
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

from app.board.navigator import nav_menu
#    nav_menu,
# html.A("Home", href='http://localhost:5000'),
layout = html.Div(id='board3', children=[

    html.H1('Hello Dash Table'),
    html.H1(id='username'),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a query and press submit'),             
    html.H1('Dash Table'),
    html.H1(id='my_data_table'),
    dcc.Textarea(
            id='textarea-state-example',
            value='Textarea content initialized\nwith multiple lines of text',
            style={'width': '100%', 'height': 200},
        ),
    html.Button('Submit', id='textarea-state-example-button', n_clicks=0),
    html.Div(id='textarea-state-example-output', style={'whiteSpace': 'pre-line'}),
    dcc.Store(id='user-store'),
], style={'width': '500'})
