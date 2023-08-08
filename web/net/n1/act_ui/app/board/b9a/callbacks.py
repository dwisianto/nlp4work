
from dash import dash_table
from dash.dependencies import Input, Output, State

from flask_login import current_user

import pandas as pd
from datetime import datetime as dt

#import logging
#LOG = logging.getLogger(__name__)
from my_cfg import my_log


#
#
#
def register_callbacks(current_app):

    @current_app.callback(
        Output('user-store', 'data'),
        Input('input-on-submit', 'value'),
        State('user-store', 'data'))
    def cur_user(args, data):
        if current_user.is_authenticated:
            return current_user.username
        else:
            return "Anonymous"

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

        from app.models import User, Tale

        tale_list = []
        for t in Tale.query.all():
            #my_log.info(" {} {} {} ".format(p.id, p.author.username, p.body))
            #if current_user.username == t.author.username:
                tale_list.append({'id':t.tale_id,
                                  'username':t.author.username,
                                  'body':t.tale_narrative})

        out_data_table = None
        if n_clicks >= 1:
            df = pd.DataFrame.from_dict(tale_list)
            #df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
            out_data_table = dash_table.DataTable(df.to_dict('records'))
        
        return out_data_table
        #return(n_clicks)
    