
#from dash import Dash, dcc, html, Input, Output, State, callback
from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State
from flask_login import current_user

import os
from datetime import datetime as dt


def register_callbacks(current_app):

    @current_app.callback(
        Output('board1-user-store', 'data'),
        Input('input-on-submit', 'value'),
        State('board1-user-store', 'data'))
    def cur_user(args, data):
        if current_user.is_authenticated:
            return current_user.username


    @current_app.callback(
        Output('username', 'children'), 
        Input('board1-user-store', 'data')
        )
    def username(data):
        if data is None:
            return ''
        else:
            return f'Username: {data}'


    @current_app.callback(
        Output('container-button-basic', 'children'),
        Input('submit-val', 'n_clicks'),
        State('input-on-submit', 'value')
    )
    def update_output(n_clicks, value):
        #value = os.environ['DATABASE_URL']
        return 'The input value was "{}" and the button has been clicked {} times'.format(
            value,
            n_clicks
        )

