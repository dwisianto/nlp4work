
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from app.board.b9.a2.seed import board_id, board_user_store_id, \
    board_button_submit_id, board_input_id, board_user_name_id, \
    board_out_container_id, board_data_table_id


#
# html.A("Home", href='http://localhost:5000'),
layout = html.Div(id=board_id, children=[
    html.H1('MainPage'),
    html.H1(id=board_user_name_id),
    html.Div(dcc.Input(id=board_input_id, type='text')),
    html.Button('Submit', id=board_button_submit_id, n_clicks=0),
    html.H1('Data Table'),
    html.H1(id=board_data_table_id),
    dcc.Store(id=board_user_store_id),
], style={'width': '500'})
