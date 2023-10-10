
import datetime
import pandas as pd
from act.actions import act_conf


#class AppDataBase():
#    DF_COL_UID, DF_COL_CASE_NUMBER, = 'uid', 'case_number'
#board_db = AppDataBase()

board_df = pd.read_excel(act_conf.app_in_xlsx, engine='openpyxl')
board_df.rename(columns={'sent_text': 'sentence_text', 'sent_keyword':'sentence_keyword'}, inplace=True)
board_df = board_df[['uid', 'file_name','sentence_keyword', 'sentence_text', ]] # 'text',


if act_conf.df_col_keywords in board_df.columns:
    keyword_list = list( set(board_df[act_conf.df_col_keywords]))
    keyword_list_dict = [ {'label':x,'value':x} for x in keyword_list]


if act_conf.df_col_file_name in board_df.columns:
    file_name_list = list( set(board_df[act_conf.df_col_file_name]))
    file_name_list_dict = [ {'label':x,'value':x} for x in file_name_list ]

#if 'date' in board_df.columns:
#    board_df['date']= board_df['date'].map(lambda x: datetime.datetime.strptime(str(x).split()[0],'%Y-%m-%d'))
#    board_df['date']= board_df["date"].apply(lambda x: x.to_pydatetime() ) # Timestamp -> Datetime
#    min_date = board_df['date'].min()
#    max_data = board_df['date'].max()
