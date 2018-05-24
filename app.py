import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

from auth.google_oauth import GoogleOAuth

server = Flask(__name__)

app = dash.Dash(__name__, server=server, url_base_pathname='/', auth='auth')
authorized_emails = ["lucas.chapin@gmail.com", "1234@example.com"]
auth = GoogleOAuth(app, authorized_emails)

@server.route("/")
def MyDashApp():
    return app.index()

app.layout = html.Div(children=[
    html.H1(children="Hello Dash"),

    html.Div(children='''
    Dash: A web application framework for Python
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 6], 'type': 'bar', 'name': 'Montreal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server()
