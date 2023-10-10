
from dash import html, dash_table, ctx

from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State
from flask_login import current_user

import pandas as pd

from my_cfg import my_config_util
from act.actions import act_conf

from app.board.b7.b71.seed import board_df

def register_callbacks(current_app):

    #
    @current_app.callback(
        Output('user-store', 'data'),
        Input(act_conf.exploration_id_message_active_cell, 'children'),
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
            return f'Dash Table - {data}'


    @current_app.callback(
        Output(act_conf.exploration_id_message_active_cell,'children'),
        Input(act_conf.exploration_id_table,'active_cell'),
        Input(act_conf.exploration_id_table, 'data')
    )
    def update_table_message_active_cell(active_cell,data):
        if active_cell:
            col = active_cell['column_id']
            row = active_cell['row']
            cellData = data[row][col]
            return html.P(f'{cellData}')
        return html.P('no cell selected')


    @current_app.callback(
        Output(act_conf.exploration_id_table, 'data'),
        Input(act_conf.exploration_id_filter_button_exe, 'n_clicks'),
        State(act_conf.exploration_id_filter_file_name, 'value'),
        State(act_conf.exploration_id_filter_keyword, 'value'),
        State(act_conf.exploration_id_filter_sentence_text, 'value'),
    )
    def update_exploration_table(n_clicks, filter1_file_name_list, filter2_keyword_list, filter3_sentence_text):

        tmp_df = board_df
        if filter1_file_name_list is None and \
            filter2_keyword_list is None and \
            len(filter3_sentence_text) == 0:
            return tmp_df.to_dict('records')

        if filter1_file_name_list is not None and len(filter1_file_name_list) >=1:
            for a_file_name in filter1_file_name_list:
                tmp_df = tmp_df[tmp_df[act_conf.df_col_file_name].str.contains(a_file_name)]

        if filter2_keyword_list is not None and len(filter2_keyword_list) >= 1:
            for a_key_word in filter2_keyword_list:
                tmp_df = tmp_df[tmp_df[act_conf.df_col_keywords].str.contains(a_key_word)]

        if filter3_sentence_text is not None and len(filter3_sentence_text) >= 1:
            tmp_snt_txt = tmp_df[act_conf.df_col_text]
            tmp_snt_flag = tmp_snt_txt.str.contains(filter3_sentence_text, regex=True)
            tmp_df = tmp_df[tmp_snt_flag]

        # out_data_table = Nonex
        # if n_clicks is not None and n_clicks >= 1:
        # my_config_util.SEED_DF
        # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
        #    out_data_table = dash_table.DataTable(my_config_util.SEED_DF.to_dict('records'))
        if tmp_df is None:
            tmp_df = board_df

        return tmp_df.to_dict('records')
