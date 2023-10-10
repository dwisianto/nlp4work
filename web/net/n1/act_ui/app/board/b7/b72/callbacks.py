

import json
import pandas as pd

from dash import ctx, html #, dash_table

from dash.dependencies import Input
from dash.dependencies import Output
# from dash.dependencies import State
# from flask_login import current_user

# from my_cfg import my_config_util
from act.actions import act_conf
from act.comment_letter3 import comment_letter_base, CommentLetterWebDb
from app.board.b7.b72.seed import  board_db


def register_callbacks(current_app):

    @current_app.callback(
        Output(act_conf.sqlite_search_query_cmd_id, 'value'),
        Input(act_conf.sqlite_search_query_dropdown_id, 'value'))
    def search_populate_query_from_example(query_dropdown_value):

        tmp_cmd = ''
        if query_dropdown_value is not None and len(query_dropdown_value) >= 1:
            tmp_var = comment_letter_base.q_var[query_dropdown_value]
            #tmp_cmd = f"""SELECT rank,* FROM {comment_letter_base.sqlite_table_uid} MATCH '{tmp_var}' ORDER_BY rank"""
            # tmp_cmd = f"""SELECT * FROM {comment_letter_base.sqlite_table_uid} MATCH {tmp_var} """
            tmp_cmd = "SELECT rank,* FROM {} WHERE {} MATCH '{}' ORDER BY RANK".format(comment_letter_base.sqlite_table_uid,
                                                                                       comment_letter_base.sqlite_col_txt,
                                                                                        tmp_var)

        return tmp_cmd


    # Output(act_conf.sqlite_search_message_id, 'children'),
    @current_app.callback(Output(act_conf.sqlite_search_table_id, 'data'),
                          Input(act_conf.sqlite_search_query_cmd_id, 'value'),
                          Input(act_conf.sqlite_search_query_example_button_id, 'n_clicks'),
                          )
    def data_table_refreshed(search_query_value, button_click_value):

        ctx_trigged_id = ctx.triggered_id if not None else 'No clicks yet'
        ctx_trigged_on_off = True if str(ctx_trigged_id) == str(act_conf.sqlite_search_query_example_button_id) else False
        ctx_dict = {'states': ctx.states,
                    'triggered': ctx.triggered,
                    'input': ctx.inputs,
                    'triggered_id': ctx_trigged_id,
                    'ctx_triggered_on_off': ctx_trigged_on_off,
                    'button_click_value': button_click_value,
                    }

        #
        #
        #
        if ctx_trigged_on_off:

            if search_query_value is not None and len(search_query_value) >= 1:
                ctx_dict['tmp_cmd'] = search_query_value
                board_db.sqlite_search_query(query_command=search_query_value)
                ctx_dict['res_df_shape']=str(board_db.db_df.shape)


        #return json.dumps(ctx_dict, indent=2)
        return board_db.db_df.to_dict('records')

    @current_app.callback(
        Output(act_conf.sqlite_search_message_id,'children'),
        Input(act_conf.sqlite_search_table_id,'active_cell'),
        Input(act_conf.sqlite_search_table_id, 'data')
    )
    def update_table_message_active_cell(active_cell,data):
        if active_cell:
            col = active_cell['column_id']
            row = active_cell['row']
            cellData = data[row][col]
            return html.P(f'{cellData}')
        return html.P('no cell selected')