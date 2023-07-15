#import dash_core_components as dcc
#import dash_html_components as html
from dash import html
from dash import dcc

layout = html.Div(id='main2', children=[
    html.A("Home", href='http://localhost:5000'),
    html.H1(children='Hello Dash'),    
    html.H1(id='username'),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit'),
    #dcc.Graph(id='my-graph'),
    dcc.Store(id='board2-user-store'),             
], style={'width': '500'})


#layout = html.Div([
#    html.Div(dcc.Input(id='input-on-submit', type='text')),
#    html.Button('Submit', id='submit-val', n_clicks=0),
#    html.Div(id='container-button-basic',
#             children='Enter a value and press submit')
#])
