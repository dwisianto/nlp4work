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
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(seconds=60) #flask-login with timeout

#
#
#
import logging
import logging.config

class MyLog:

    @staticmethod
    def get_handler(log_path, name='default'):
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

my_log = MyLog.get_handler(log_path=os.path.join(ACT_CONFIG['log_dir'],'my_log.log'))