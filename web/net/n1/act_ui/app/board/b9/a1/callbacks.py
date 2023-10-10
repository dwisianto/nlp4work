
#import os
#from datetime import datetime as dt
#from dash import Dash, dcc, html, Input, Output, State, callback

from dash.dependencies import Input, Output, State
from flask_login import current_user

from app.board.b9.a1.seed import board_id, board_user_store_id, board_button_submit_id, board_input_id, board_user_name_id, board_out_container_id

def register_callbacks(current_app):

    @current_app.callback(
        Output(board_user_store_id, 'data'),
        Input(board_input_id, 'value'),
        State(board_user_store_id, 'data'))
    def cur_user(args, data):
        if current_user.is_authenticated:
            return current_user.username


    @current_app.callback(
        Output(board_user_name_id, 'children'),
        Input(board_user_store_id, 'data')
        )
    def username(data):
        if data is None:
            return ''
        else:
            return f'Username: {data}'


    @current_app.callback(
        Output(board_out_container_id, 'children'),
        Input(board_button_submit_id, 'n_clicks'),
        State(board_input_id, 'value')
    )
    def update_output(n_clicks, value):
        #value = os.environ['DATABASE_URL']
        return 'The input value was "{}" and the button has been clicked {} times'.format(
            value,
            n_clicks
        )

