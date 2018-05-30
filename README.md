# Dash Google OAuth
Basic example of using Google OAuth to authenticate and view a [Dash](https://dash.plot.ly/) app. Uses [flask dance](https://github.com/singingwolfboy/flask-dance) and a modified version of Plotly's own [dash auth](https://github.com/plotly/dash-auth) for authentication.

Steps to try this out yourself (after installing requirements):
1. Follow the [Flask Dance Guide](http://flask-dance.readthedocs.io/en/latest/quickstarts/google.html) to create an app on the google admin console
2. Replace the variables for *app.server.config["GOOGLE_OAUTH_CLIENT_ID"]* and *app.server.config["GOOGLE_OAUTH_CLIENT_SECRET"]* in [google_oauth.py](./auth/google_oauth.py)
3. Replace authorized_emails from [app.py](./app.py) with whatever google authenticated emails you want to test with, or perhaps get these from a database.
4. Run `python app.py` and try it out! Open localhost in an incogntio window if you're already authenticated.
