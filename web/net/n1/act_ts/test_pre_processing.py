#
#
#
import pandas as pd
import pytest
import pprint as pp
import logging
LOG = logging.getLogger(__name__)


#
#
#
import os
from pypdf import PdfReader
# import shlex
# import shutil
# import subprocess

# https://www.sec.gov/comments/s7-04-23/s70423.htm


@pytest.mark.skip
class TestPandasFrame:


    @pytest.mark.skip
    @pytest.mark.order(1)
    def test_pre_process_i1_config(self, act_config):
        #LOG.info(" act_config ")
        #LOG.info(pp.pformat(str(act_config)))

        LOG.info(act_config.dat_dir)

        file_dir = os.path.join(act_config.dat_dir, 's70423')
        for a_file_name in os.listdir( file_dir ):
            LOG.info( a_file_name )

            reader = PdfReader(os.path.join(file_dir,a_file_name))
            number_of_pages = len(reader.pages)
            LOG.info(number_of_pages)
            page = reader.pages[0]
            page_text = page.extract_text()
            #LOG.info(pagettext)



    def test_pre_process_i2_dat_frame(self, act_config):
        LOG.info(" act_config ")
        LOG.info(pp.pformat(str(act_config)))



