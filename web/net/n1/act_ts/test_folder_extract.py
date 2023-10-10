
#
#
#
import os
import pytest
import pprint as pp
import pandas as pd

from act.folder_extract import ExtractFromFolder
from act.comment_letter3 import CommentLetterSearch

import logging
LOG = logging.getLogger(__name__)


#
#
# @pytest.mark.skip
class TestFolderExtract:

    @pytest.mark.order(1)
    def test_folder_extract_i1_config(self, act_config):
        LOG.info(" act_config ")
        LOG.info(pp.pformat(str(act_config)))
        LOG.info(act_config.act_ts)
        LOG.info(act_config.act_ui)

    @pytest.mark.order(2)
    def test_folder_extract_i2(self, act_config, my_config):

        cls = ExtractFromFolder()
        LOG.info(" my_config ")
        LOG.info(pp.pformat(my_config))
        LOG.info(pp.pformat(act_config))
        filepath_list = [
            os.path.join(my_config['fdrive'], filepath)
            for filepath in os.listdir(my_config['fdrive'])
        ]
        filenames = [os.path.split(filename)[-1] for filename in filepath_list]
        df = pd.DataFrame({'file_path': filepath_list, 'file_name': filenames})
        df['text'], df['page_number'] = zip(*df['file_path'].map(cls.extract_text_pdf_html))
        df = df.drop(columns=['file_path']).copy()
        exploded1 = df.explode(['text', 'page_number'])
        exploded1['sentence_number'] = list(range(len(exploded1)))
        # exploded1['uid'] = exploded1.index.values.tolist()
        exploded1['case_number'] = exploded1.index.values.tolist()
        exploded1['sent_text'] = exploded1['text'].astype(str).apply(lambda x: cls.char_pos_match(x)[0])
        exploded1['sent_keyword'] = exploded1['text'].astype(str).apply(lambda x: cls.char_pos_match(x)[1])
        exploded1 = exploded1[exploded1['sent_text'].map(lambda d: len(d)) > 0].copy()
        exploded1 = exploded1.reset_index()
        exploded1['uid'] = exploded1.index.values.tolist()
        #exploded_pdf = exploded1[exploded1['file_name'].astype(str).str.endswith('.pdf')].copy()
        #exploded_htm = exploded1[exploded1['file_name'].astype(str).str.endswith('.htm')].copy()
        LOG.info(exploded1.shape)
        LOG.info(exploded1.columns)
        LOG.info(str(exploded1))
        LOG.info(pp.pformat(exploded1))


        os.makedirs(my_config["dat_dir"], exist_ok=True)
        exploded1.to_excel(os.path.join(my_config["out_dir"],"letters_scrape_from_pdf_htm.xlsx"),engine='xlsxwriter', index=True)
        #exploded_pdf.to_excel(os.path.join(my_config["out_dir"],"letters_scrape_from_pdf_only.xlsx"),engine='xlsxwriter', index=True)
        #exploded_htm.to_excel(os.path.join(my_config["out_dir"],"letters_scrape_from_htm_only.xlsx"),engine='xlsxwriter', index=True)


        exploded23 = exploded1[['uid','sent_text']]
        LOG.info(exploded23.shape)
        LOG.info(exploded23.index)
        LOG.info(exploded23.columns)
        LOG.info(exploded23)

        my_base = CommentLetterSearch( in_df=exploded23 )
        my_base.sqlite_search_setup(file_dir=my_config["out_dir"], file_name='comment_letter_search.sqlite')
        my_base.sqlite_search_command(file_dir=my_config["out_dir"], file_name='comment_letter_search.sqlite')
        LOG.info( my_config["out_dir"] )