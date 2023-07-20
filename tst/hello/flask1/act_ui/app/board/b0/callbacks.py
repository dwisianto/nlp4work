
from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State
from flask_login import current_user

from datetime import datetime as dt

def register_callbacks(current_app):

    @current_app.callback(
        Output('user-store', 'data'),
        Input('input-on-submit', 'value'),
        State('user-store', 'data'))
    def cur_user(args, data):
        if current_user.is_authenticated:
            return current_user.username
        else:
            return "Guest"

    @current_app.callback(Output('username', 'children'), 
                        Input('user-store', 'data'))
    def username(data):
        if data is None:
            return ''
        else:
            return f'Username: {data}'
