
import datetime
import pandas as pd
from act.actions import act_conf

from act.comment_letter3 import board_db





if act_conf.df_col_keywords in board_db.df.columns:
    keyword_list = list( set(board_db.df[act_conf.df_col_keywords]))
    keyword_list_dict = [ {'label': x, 'value':x} for x in keyword_list]

if act_conf.df_col_file_name in board_db.df.columns:
    file_name_list = list( set(board_db.df[act_conf.df_col_file_name]))
    file_name_list_dict = [ {'label': x, 'value':x} for x in file_name_list ]

#if 'date' in board_df.columns:
#    board_df['date']= board_df['date'].map(lambda x: datetime.datetime.strptime(str(x).split()[0],'%Y-%m-%d'))
#    board_df['date']= board_df["date"].apply(lambda x: x.to_pydatetime() ) # Timestamp -> Datetime
#    min_date = board_df['date'].min()
#    max_data = board_df['date'].max()


