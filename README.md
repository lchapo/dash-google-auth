# Deprecation Warning
This project is no longer actively maintained and is incompatible with newer versions of Dash (>=1.0). Please consider forking this repo or see the [Dash docs](https://dash.plotly.com/authentication) on officially supported authentication mechanisms.

# Dash Google Auth

Dash Google Auth is a simple library using Google OAuth to authenticate and
view a [Dash](https://dash.plot.ly/) app.

This Library uses [Flask Dance](https://github.com/singingwolfboy/flask-dance)
and a modified version of Plotly's own [dash auth](https://github.com/plotly/dash-auth)
for authentication.

## Basic Use

Authentication can be added to your Dash application using the `GoogleOAuth`
class, i.e.

```python
from dash import Dash
from flask import Flask
from dash_google_auth import GoogleOAuth

server = Flask(__name__)
server.config.update({
  'GOOGLE_OAUTH_CLIENT_ID': ...,
  'GOOGLE_OAUTH_CLIENT_SECRET': ...,
})

app = Dash(__name__, server=server, url_base_pathname='/', auth='auth')

authorized_emails = [...]
additional_scopes = [...]
auth = GoogleOAuth(app, authorized_emails, additional_scopes)

# your Dash app here :)
...
```

## Example
Steps to try this out yourself:

1. Install the `dash-google-auth` library using `pip`:

    ```bash
    $ pip install dash-google-auth
    ```

2. Follow the [Flask Dance Guide](http://flask-dance.readthedocs.io/en/latest/quickstarts/google.html)
   to create an app on the google admin console

3. Make a copy of [app.py](https://github.com/lucaschapin/dash-google-auth/blob/master/app.py)
   and set the variables (or set the corresponding environment variables):
    ```python
    server.config["GOOGLE_OAUTH_CLIENT_ID"] = ...
    server.config["GOOGLE_OAUTH_CLIENT_SECRET"] = ...
    ```
   with values from the Google OAuth 2 client you should have set up in step 1.
   If you've set these up properly, you can find them at
   [APIs & Services > Credentials](https://console.developers.google.com/apis/credentials)
   under the section **OAuth 2.0 client IDs**.

4. Replace `authorized_emails` in `app.py` with whatever
   Google emails you want to grant access to your app. In production, I'd
   recommend getting these from a database instead.

5. Run `python app.py` and open [localhost](http://localhost:8050/) in a
   browser window to try it out! If the app loads automatically without
   prompting a Google login, that means you're already authenticated -- try
   using an incognito window in this case if you want to see the login
   experience for a new user.
