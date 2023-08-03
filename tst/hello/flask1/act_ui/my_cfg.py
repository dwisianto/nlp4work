#
# Keep this file and other files used by the create_app function free of inner-project import statements
# to help prevent circular imports.
# Setting up cache in a separate cache.py file similar to this config.py file is very helpful.
#

import os
import datetime # flask-login timeout

from act.actions import ACT_CONFIG


def get_sqlite_uri():
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_name = os.environ['DATABASE_URL'].split('/')[-1]
    return f'sqlite:///{basedir}/{db_name}'


class MyConfigObject:
    SQLALCHEMY_DATABASE_URI = get_sqlite_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ['SECRET_KEY']
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(seconds=60)  # flask-login with timeout


class MyDebug:
    dash_debug = False
    dash_auto_reload = False


my_debug = MyDebug()


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

