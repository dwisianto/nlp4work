#
# Keep this file and other files used by the create_app function free of inner-project import statements
# to help prevent circular imports.
# Setting up cache in a separate cache.py file similar to this config.py file is very helpful.
#

import os
import pandas as pd
import datetime # flask-login timeout

from act.actions import ACT_CONFIG

class MyConfigUtil:

    # Seed Excel File
    SEED_XLSX = os.environ['SEED_XLSX']
    SEED_FULL_PATH=os.environ['SEED_XLSX_FULL_PATH']

    # Plotly Dash
    DASH_DEBUG = False
    DASH_DEBUG_AUTO_RELOAD = False

    @staticmethod
    def get_sqlite_uri():
        basedir = os.path.abspath(os.path.dirname(__file__))
        db_name = os.environ['DATABASE_URL'].split('/')[-1]
        return f'sqlite:///{basedir}/{db_name}'

    def __init__(self):
        self.SEED_DF=pd.read_excel(os.path.join(self.SEED_FULL_PATH,self.SEED_XLSX))


my_config_util = MyConfigUtil()



class MyConfigObject:
    SQLALCHEMY_DATABASE_URI = MyConfigUtil.get_sqlite_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ['SECRET_KEY']

    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=3)  # flask-login with timeout
    CORS_HEADERS = 'Content-Type'
    LOGIN_DISABLED = False

    LOC_TEMPLATE = 'template/t3'
    LOC_STATIC = 'static/s3'
    LOC_STATIC_URL_PATH = '/static/'
    LOC_STATIC_FAVICON='static/s3/favicon'
    LOC_STATIC_FAVICON_NAME = 'favicon.ico'



#
#
#
import datetime
import logging
import logging.config


class MyLog:

    @staticmethod
    def get_handler(log_path, name='default'):

        MyLog.create_dir_when_missing(log_path)

        logging.config.dictConfig({
            'version': 1,
            'formatters': {
                'default': {'format': '%(asctime)s - %(levelname)s - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'}
            },
            'handlers': {
                'console': {
                    'level': 'INFO',
                    'class': 'logging.StreamHandler',
                    'formatter': 'default',
                    'stream': 'ext://sys.stdout'
                },
                'file': {
                    'level': 'INFO',
                    'class': 'logging.handlers.TimedRotatingFileHandler',
                    'formatter': 'default',
                    'when': 'midnight',
                    'filename': log_path,
                    'backupCount': 5
                }
            },
            'loggers': {
                'default': {
                    'level': 'INFO',
                    'handlers': ['console', 'file']
                }
            },
            'disable_existing_loggers': False
        })
        return logging.getLogger(name)

    @staticmethod
    def create_dir_when_missing(log_dir_path):
        log_dir_path_basedir = os.path.dirname(log_dir_path)
        if not os.path.exists(log_dir_path_basedir):
            os.mkdir(log_dir_path_basedir)


my_log_file_name = 'my_app_'+datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')+'.log'
my_log = MyLog.get_handler(log_path=os.path.join(ACT_CONFIG['log_ui'], my_log_file_name))
