
from dash import dash_table
from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State
from flask_login import current_user

import pandas as pd
from datetime import datetime as dt

def register_callbacks(current_app):

    @current_app.callback(
        Output('user-store', 'data'),
        Input('input-on-submit', 'value'),
        State('user-store', 'data'))
    def cur_user(args, data):
        if current_user.is_authenticated:
            return current_user.username

    @current_app.callback(Output('username', 'children'), 
                        Input('user-store', 'data'))
    def username(data):
        if data is None:
            return ''
        else:
            return f'Username: {data}'

    # State('input-on-submit', 'data')
    #def update_graph(selected_dropdown_value, value, data):
    @current_app.callback(
        Output('my_data_table', 'children'),
        Input('submit-val', 'n_clicks'),
        )
    def update_graph(n_clicks):
        
        out_data_table = None
        if n_clicks >= 1:
            df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
            out_data_table = dash_table.DataTable(df.to_dict('records'))
        
        return out_data_table
        #return(n_clicks)

    #@current_app.callback(
    #    Output('my_data_table', 'children'),
    #    Output('container-button-basic', 'children'),
    #    Input('submit-val', 'n_clicks'),
    #    State('input-on-submit', 'value')
    #)
    #def update_output(n_clicks, value):
    #    
    #    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
    #        
    #    out_data_table = dash_table.DataTable(df.to_dict('records'))
    #    out_msg = 'The query is "{}" and the button has been clicked {} times'.format(value,n_clicks)
    #    return out_data_table, out_msg


    @current_app.callback(
        Output('textarea-state-example-output', 'children'),
        Input('textarea-state-example-button', 'n_clicks'),
        State('textarea-state-example', 'value')
    )
    def update_output(n_clicks, value):
        if n_clicks > 0:
            return 'You have entered: \n{}'.format(value)