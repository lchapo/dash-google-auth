from flask import (
    redirect,
    url_for,
    Response,
    abort,
)
from flask_dance.contrib.google import (
    make_google_blueprint,
    google,
)

from .auth import Auth


class GoogleOAuth(Auth):
    def __init__(self, app, authorized_emails, additional_scopes=None):
        super(GoogleOAuth, self).__init__(app)
        google_bp = make_google_blueprint(
            scope=[
                "https://www.googleapis.com/auth/userinfo.email",
                "https://www.googleapis.com/auth/userinfo.profile",
            ] + (additional_scopes if additional_scopes else []),
            offline=True,
            reprompt_consent=True,
        )
        app.server.register_blueprint(google_bp, url_prefix="/login")
        self.authorized_emails = authorized_emails

    def is_authorized(self):
        if not google.authorized:
            # send to google login
            return False

        resp = google.get("/oauth2/v2/userinfo")
        assert resp.ok, resp.text

        email = resp.json()["email"]
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
