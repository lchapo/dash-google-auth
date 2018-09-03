from .auth import Auth

import os

from flask import Flask, redirect, url_for, render_template, Response, abort
from flask_dance.contrib.google import make_google_blueprint, google
from werkzeug.contrib.fixers import ProxyFix

class GoogleOAuth(Auth):
    def __init__(self, app, authorized_emails):
        Auth.__init__(self, app)
        app.server.wsgi_app = ProxyFix(app.server.wsgi_app)
        app.server.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
        app.server.config["GOOGLE_OAUTH_CLIENT_ID"] = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
        app.server.config["GOOGLE_OAUTH_CLIENT_SECRET"] = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
        google_bp = make_google_blueprint(
            scope=["profile", "email"],
            offline=True,
            reprompt_consent=True,
        )
        app.server.register_blueprint(google_bp, url_prefix="/login")
        self.authorized_emails = authorized_emails

    def is_authorized(self):
        if not google.authorized:
            # send to google login
            return False

        resp = google.get("/plus/v1/people/me")
        assert resp.ok, resp.text

        email = resp.json()["emails"][0]["value"]
        if email in self.authorized_emails:
            # send to index
            return True
        else:
            # unauthorized email
            return abort(403)

    def login_request(self):
        # send to google auth page
        return redirect(url_for("google.login"))

    def auth_wrapper(self, f):
        def wrap(*args, **kwargs):
            if not self.is_authorized():
                return Response(status=403)

            response = f(*args, **kwargs)
            return response
        return wrap

    def index_auth_wrapper(self, original_index):
        def wrap(*args, **kwargs):
            if self.is_authorized():
                return original_index(*args, **kwargs)
            else:
                return self.login_request()
        return wrap
