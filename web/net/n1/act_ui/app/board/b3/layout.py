
from dash import dcc
from dash import html
from dash import dash_table
import dash_bootstrap_components as dbc


from app.board.navigator import nav_menu

layout = html.Div(id='board2', children=[
    html.H1(id='username'),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Press press submit'),             
    html.H1('Dash Table'),
    html.H1(id='my_data_table'),
    dcc.Store(id='user-store'),
], style={'width': '500'})






