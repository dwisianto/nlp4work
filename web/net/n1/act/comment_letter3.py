
import os
import pprint
import sqlite3

import logging

import pandas as pd

LOG = logging.getLogger(__name__)

from act.actions import act_conf



class CommentLetterBase:

    df_col_author = 'author'
    df_col_text   = 'text'
    df_col_uid    = 'uid'
    df_col_sent_text = 'sent_text'
    df_col_sent_keyword = 'sent_keyword'


    sqlite_col_uid = 'uid'
    sqlite_col_txt = 'sent_text'
    sqlite_table_uid = 'comments_txt'
    sqlite_file_name = 'comment_letter_search.sqlite'

    q_var = {
        'q0': 'fee*',
        'q1': 'fee',
        'q2': '^The',
        'q3': '^investor',
        'q4': 'The OR scenario',  # Boolean AND, OR, NOT operators between tokens
        'q5': 'The AND fee and cost*',  # Hybrid Query
        'q6': 'A AND the OR a NOT of*',
        'q7': 'fee*',
        'q8': 'price*',
        'q9': 'sent_text: fee',  # search field in the query itself
    }

    q_cmd_order = {
        'q0': f"""SELECT * FROM {sqlite_table_uid}""",
        'q1': f"""SELECT * FROM {sqlite_table_uid} WHERE {sqlite_col_txt} MATCH '{q_var['q1']}'""",
        'q2': f"""SELECT * FROM {sqlite_table_uid} WHERE {sqlite_col_txt} MATCH '{q_var['q2']}'""",
        'q3': f"""SELECT * FROM {sqlite_table_uid} WHERE {sqlite_col_txt} MATCH '{q_var['q3']}'""",
        'q4': f"""SELECT rank,* FROM {sqlite_table_uid} WHERE {sqlite_col_txt} MATCH '{q_var['q4']}' ORDER BY RANK""",
        'q5': f"""SELECT rank,* FROM {sqlite_table_uid} WHERE {sqlite_col_txt} MATCH '{q_var['q5']}' ORDER BY RANK""",
        'q6': f"""SELECT rank,* FROM {sqlite_table_uid} WHERE {sqlite_col_txt} MATCH '{q_var['q6']}' ORDER BY RANK""",
        'q7': f"""SELECT rank,* FROM {sqlite_table_uid} WHERE {sqlite_col_txt} MATCH '{q_var['q7']}' ORDER BY RANK""",
        'q8': f"""SELECT rank,* FROM {sqlite_table_uid} WHERE {sqlite_col_txt} MATCH '{q_var['q8']}' ORDER BY RANK""",
        'q9': f"""SELECT rank,* FROM {sqlite_table_uid} WHERE {sqlite_col_txt} MATCH '{q_var['q9']}' ORDER BY RANK""",
    }

    def __init__(self):
        pass


        #q_var = { 'q1': 'fee*',
        #    'q2': '^gold*',
        #    'q3': '^gold* OR oil* OR gas*',
        #    'q4': '^The AND fee* OR cost*',
        #    'q5': 'oil* OR gas* NOT green* NOT wind*',
        #    'q6': 'percent*',        }

comment_letter_base = CommentLetterBase()


class CommentLetterSearch(CommentLetterBase):

    def __init__(self, in_df):
        super().__init__()
        self.df = in_df

    def sqlite_search_setup(self, file_dir, file_name):

        # remove the database if exists
        out_sqlite_full_name = os.path.join(file_dir, file_name)
        os.remove(out_sqlite_full_name) if os.path.exists(out_sqlite_full_name) else None
        os.mkdir(file_dir) if not os.path.exists(file_dir) else None
        LOG.info(" out_sqlite_full_name : {} ".format(out_sqlite_full_name))

        # prepare the dataframe such as lower casing
        self.df[self.df_col_uid] = self.df[self.sqlite_col_uid].astype(str)
        self.df[self.df_col_text] = self.df[self.sqlite_col_txt].str.lower()

        #self.df[self.df_col_sent_keyword] = self.df[self.df_col_sent_keyword].str.lower()

        # create an sqlite database
        db = sqlite3.connect(out_sqlite_full_name)
        db_cursor = db.cursor()

        #
        # create table
        #sql_cmd_init = 'create virtual table {t0} using fts5({f1},{f2}, tokenize="trigram");'.format(
        #sql_cmd_init = 'create virtual table {t0} using fts5({f1},{f2}, tokenize="porter unicode61");'.format(
        sql_cmd_init = 'create virtual table {t0} using fts5({f1},{f2});'.format(
            t0=self.sqlite_table_uid,
            f1=self.sqlite_col_uid,
            f2=self.sqlite_col_txt,
        )
        db_cursor.execute(sql_cmd_init)

        sql_cmd_insert = 'insert into {t0} ({f1}, {f2}) values ({f0});'.format(
            t0=self.sqlite_table_uid,
            f1=self.sqlite_col_uid,
            f2=self.sqlite_col_txt,
            f0='?,?')

        db_cursor.executemany(sql_cmd_insert,
                              self.df[[self.sqlite_col_uid, self.sqlite_col_txt]]
                              .to_records(index=False))

        db.commit()
        db_cursor.close()

    def sqlite_search_command(self, file_dir, file_name):

        out_sqlite_full_name = os.path.join(file_dir, file_name)
        db = sqlite3.connect(out_sqlite_full_name)
        db_cursor = db.cursor()

        for q_key, q_cmd in self.q_cmd_order.items():
            LOG.info('q:'+ self.q_var[q_key])
            LOG.info('q_cmd:'+q_cmd)
            res = db_cursor.execute(q_cmd).fetchall()
            LOG.info('res_len: '+str(len(res)) + " -> " + str(res[0]) if len(res) > 1 else None)


#
#
#
class CommentLetterWebDb(CommentLetterBase):

    def __init__(self, ):
        super().__init__()
        self.db_sqlite = sqlite3.connect(act_conf.app_in_fts, check_same_thread=False)
        self.db_df = None

        xlsx_df = pd.read_excel(act_conf.app_in_xlsx, engine='openpyxl')
        xlsx_df.rename(columns={'sent_text': 'sentence_text', 'sent_keyword': 'sentence_keyword'}, inplace=True)
        xlsx_df['uid'] = xlsx_df['uid'].astype(int)
        self.df = xlsx_df[['uid', 'file_name', 'sentence_keyword', 'sentence_text', ]]  # 'text',

    def initialize_table(self):
        q_tmp = 'q8'
        db_cursor = self.db_sqlite.cursor()
        q_key = self.q_var[q_tmp]
        q_cmd = self.q_cmd_order[q_tmp]
        # for q_key, q_cmd in self.q_cmd_order.items(): print('q:'+self.q_var[q_key])
        res = db_cursor.execute(q_cmd).fetchall()
        self.augment_search_response(res)

    def sqlite_search_query(self, query_command):
        db_cursor = self.db_sqlite.cursor()
        #query_command ='SELECT * FROM comments_txt'
        #query_command = "SELECT * FROM comments_txt WHERE sent_txt MATCH 'fee*'"
        #query_command = self.q_cmd_order['q1']
        res = db_cursor.execute(query_command).fetchall()
        self.augment_search_response(res)
        return self.db_df

    def augment_search_response(self, res):
        res_df = pd.DataFrame(res)
        res_df.columns = [act_conf.df_col_score, act_conf.df_col_uid, act_conf.df_col_text]
        res_df = res_df.drop(act_conf.df_col_text, axis=1)
        res_df['uid'] = res_df['uid'].astype(int)

        # self.db_df = pd.merge(self.db_df, in_app_df, how="left")
        self.db_df = res_df.merge(self.df, left_on='uid', right_on='uid', how="left")

board_db = CommentLetterWebDb()
board_db.initialize_table()