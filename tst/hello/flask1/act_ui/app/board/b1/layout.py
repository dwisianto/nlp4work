
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from app.board.navigator import nav_menu


# html.A("Home", href='http://localhost:5000'),
layout = html.Div(id='board1', children=[
    nav_menu,    
    html.H1(children='Hello Dash Button'),    
    html.H1(id='username'),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit'),
    #dcc.Graph(id='my-graph'),
    dcc.Store(id='board1-user-store'),             
], style={'width': '500'})


#layout = html.Div([
#    html.Div(dcc.Input(id='input-on-submit', type='text')),
#    html.Button('Submit', id='submit-val', n_clicks=0),
#    html.Div(id='container-button-basic',
#             children='Enter a value and press submit')
#])
