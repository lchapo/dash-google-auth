# Dash Google Auth
Basic example of using Google OAuth to authenticate and view a [Dash](https://dash.plot.ly/) app. Uses [flask dance](https://github.com/singingwolfboy/flask-dance) and a modified version of Plotly's own [dash auth](https://github.com/plotly/dash-auth) for authentication.

Steps to try this out yourself (after installing requirements):
1. Follow the [Flask Dance Guide](http://flask-dance.readthedocs.io/en/latest/quickstarts/google.html) to create an app on the google admin console
2. Replace the variables for *server.config["GOOGLE_OAUTH_CLIENT_ID"]* and *server.config["GOOGLE_OAUTH_CLIENT_SECRET"]* in [__init__.py](./app/__init__.py) with values from the Google OAuth 2 client you should have set up in step 1
3. Replace authorized_emails from [__init__.py](./app/__init__.py) with whatever google authenticated emails you want to test with. You could also get these from a database.
4. Run `python app.py` and open localhost in a browser window to try it out! Dash uses port 8050 by default, so if you haven't changed this you'd want to go [here](http://localhost:8050/) If the app loads automatically without prompting a google login, that means you're already authenticated -- try using an incogntio window in this case if you want to see the login experience for a new user.
