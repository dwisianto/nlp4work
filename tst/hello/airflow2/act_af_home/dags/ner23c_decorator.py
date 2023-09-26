
from airflow.decorators import dag, task
from airflow.operators.python import ExternalPythonOperator, PythonVirtualenvOperator

import sys
import logging
import tempfile
import pendulum
import datetime as dt


log = logging.getLogger(__name__)

PYTHON = sys.executable

BASE_DIR = tempfile.gettempdir()


# PYTHONPATH
@dag(
    dag_id='ner23c',
    schedule='30 * * * *',
    start_date=dt.datetime(2023,6,20),
    catchup=False,
    tags=["ner"],
    max_active_runs=1
)
def ner23c():

    s101_uid = 's101'

    @task(
        task_id=s101_uid,
        params={
            'a':1,
            'lookback':1,
        }
    )
    def s101(ds=None, ts=None, params=None):

        ds_end=str(dt.date.fromisoformat(ds))
        ds_start=str(dt.date.fromisoformat(ds) - dt.timedelta(weeks=params['lookback']))

        logging.info('ds_start : '+ds_start)
        logging.info(ds)
        logging.info(type(ds))
        logging.info(ts)
        logging.info(type(ts))
        logging.info('ds_end    : '+ds_end)

    s102_uid = 's102'
    @task.external_python(
        task_id=s102_uid,
        python='/opt/homebrew/anaconda3/envs/p9net8/bin/python'
    )
    def s102(ds=None, ts=None, params=None):
        """
        :param ds:
        :param ts:
        :param params:
        :return:
        """

        import sys
        import logging
        from time import sleep

        ########## MY CODE ##########
        import numpy as np
        import pandas as pd
        d = {'col1': [1, 2], 'col2': [3, 4]}
        df = pd.DataFrame(data=d)
        print(df)
        a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        print(a)
        # a= 10
        return a
        ########## XXXXX MY CODE XXXXX ##########

        #logging.info(f"sys.executable {sys.executable} ")
        logging.info("Start")
        for _ in range(3):
            sleep(1)
        logging.info("Finished")

    #s103_uid='s103' external_classic=ExternalPythonOperator(task_id=s103_uid, python='', python_callable='')

    s101() >> s102()

ner23c()