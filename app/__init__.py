import os

from flask import Flask 
from dash import Dash

from .google_oauth import GoogleOAuth

# configure app
server = Flask(__name__)
app = Dash(
	__name__,
	server=server,
	url_base_pathname='/',
	auth='auth',
)

# configure google oauth using environment variables
server.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
server.config["GOOGLE_OAUTH_CLIENT_ID"] = os.environ["GOOGLE_OAUTH_CLIENT_ID"]
server.config["GOOGLE_OAUTH_CLIENT_SECRET"] = os.environ["GOOGLE_OAUTH_CLIENT_SECRET"]

# allow for insecure transport for local testing (remove in prod)
server.config["OAUTHLIB_RELAX_TOKEN_SCOPE"] = 1
server.config["OAUTHLIB_INSECURE_TRANSPORT"] = 1

# designate list of authorized emails
authorized_emails = [
	"lucas.chapin@gmail.com",
	"1234@example.com",
]

auth = GoogleOAuth(
    app,
    authorized_emails,
)
