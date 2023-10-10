
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

nav_menu = dbc.Nav(
    [
        dbc.NavLink("Home", href="/board0",external_link=True, active=True),
        dbc.NavLink("Board1", href="/board1", external_link=True, disabled=True),
        dbc.NavLink("Board2", href="/board2", external_link=True),
        dbc.NavLink("Logout", href="/logout", external_link=True),
    ]
)

# html.A("Home", href='http://localhost:5000'),
layout = html.Div(id='main', children=[
    nav_menu,    
    html.H1(id='username'),
    html.H1('Dash Table'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph'),
    dcc.Store(id='user-store'),
], style={'width': '500'})
