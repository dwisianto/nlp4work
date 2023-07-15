
#
# Standard Toolboxes
#
import os
import sys
import pytest
import pathlib
import datetime
import pprint as pp


#
# Customization
#
from act.actions import ACT_CONFIG, act_conf


sys.path.insert(0, os.path.join(ACT_CONFIG['top_work'], 'act_ui'))
pp.pprint(sys.path)


#
# https://pawamoy.github.io/posts/save-pytest-logs-as-artifact-gitlab-ci/
# https://stackoverflow.com/questions/41400722/pytest-implementing-a-logfile-per-test-method
##################
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_setup(item):

    # default log organization using the datetime object
    name_raw = datetime.datetime.now().strftime('%Y%m%dT_%H%M%S')
    name4cat = str(datetime.datetime.now().strftime('%Y'))
    name4dir = str(datetime.datetime.now().strftime('%m'))
    name4act = str(datetime.datetime.now().strftime('%d'))
    name4tst = ''
    # split the test name using the underscore symbol
    if hasattr(item, '_request'):
        name_raw = str(item._request.node.name)
        name_list = name_raw.split("_")
        name4cat = name_list[1].lower() if len(name_list) > 1 else ""  # category
        name4dir = name_list[2].lower() if len(name_list) > 2 else ""  # directory
        name4act = name_list[3].lower() if len(name_list) > 3 else ""  # action
        name4tst = "_".join(name_list[4:]) if len(name_list) > 4 else ""
        name4tst = name4tst.lower()

    # full name
    filename = pathlib.Path(ACT_CONFIG['log_dir'],
                            name4cat, name4dir, name4act, name4tst,
                            f"{datetime.datetime.now().strftime('%Y%m%dT_%H%M%S')}.{name_raw}.log"
                            )
    # pp.pprint(filename)

    config = item.config
    logging_plugin = config.pluginmanager.get_plugin('logging-plugin')
    logging_plugin.set_log_path(str(filename))
    yield


@pytest.fixture(scope="function")
def my_config(request):
    """
    now is the current time
    pytest test name
    :param request:
    :return:
    """

    # ds1
    my_dict = {'time_now': f"{datetime.datetime.now().strftime('%Y%m%dT_%H%M%S')}",
               'test_name': str(request.function.__name__)
               }
    my_dict.update(ACT_CONFIG)

    #
    # [] environment variables
    #
    os.environ['DAT_LOC'] = os.getenv("HOME") + '/db'
    os.environ['JAVA_HOME'] = '/dsw/software/java/jdk/j1102'
    os.environ['DATABASE_URL'] = 'sqlite:///${PWD}/migrations_db.sqlite'
    os.environ['FLASK_ENV']='development'
    os.environ['FLASK_APP']='my_app'
    os.environ['SECRET_KEY']='my_secret'
    return my_dict


@pytest.fixture(scope="function")
def act_config(request):
    return act_conf


#@pytest.fixture()
#def app_fixture():
#    app.config['TESTING'] = True
#
#    with app.app_context():
#        yield