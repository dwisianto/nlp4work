
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from app.board.navigator import nav_menu

#
# html.A("Home", href='http://localhost:5000'),
layout = html.Div(id='main', children=[
    nav_menu,    
    html.H1('MainPage'),
    html.H1(id='username'),
    html.Div(dcc.Input(id='input-on-submit', type='text')),   
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.H1('Data Table'),
    html.H1(id='my_data_table'),
    dcc.Store(id='user-store'),
], style={'width': '500'})
