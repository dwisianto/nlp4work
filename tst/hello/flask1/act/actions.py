
#
# [] Constants
#
import os
import pathlib


#
# [] Constants
#
TOP_WORK = pathlib.Path(__file__).parents[1].absolute().__str__()
TOP_SPACE = pathlib.Path(__file__).resolve().parents[5].absolute().__str__()
TOP_LST = TOP_WORK.split('/')
ACT = {
    'work': TOP_WORK,
    'space': TOP_SPACE,
    'project': TOP_LST[-4],
    'tst': TOP_LST[-3],
    'lot': TOP_LST[-2],
    'exp': TOP_LST[-1],
    'src': "src",
    'log': "log",
    'out': "out",
    'dat': "dat"
}

ACT_CONFIG = {
    'top_work': ACT['work'],
    'top_space': ACT['space'],
    'top_dir': os.path.abspath(os.path.join(ACT['space'], ACT['project'])),
    'src_dir': os.path.abspath(os.path.join(ACT['space'], ACT['project'], ACT['src'], ACT['lot'])),
    'dat_dir': os.path.abspath(os.path.join(ACT['space'], ACT['project'], ACT['dat'], ACT['lot'], ACT['exp'])),
    'act_dir': os.path.abspath(os.path.join(ACT['space'], ACT['project'], ACT['tst'], ACT['lot'], ACT['exp'])),
    'log_dir': os.path.abspath(os.path.join(ACT['space'], ACT['project'], ACT['log'], ACT['lot'], ACT['exp'])),
    'out_dir': os.path.abspath(os.path.join(ACT['space'], ACT['project'], ACT['out'], ACT['lot'], ACT['exp'])),
    'JAVA_HOME': os.getenv('JAVA_HOME')
}


class ActConfig:
    SQLITE_FILE_DIR = os.path.join(os.environ['MY_DAT'], 'xcl', 'c1a')
    SQLITE_FILE_NAME = 'cost_passages_2023_05_07.sqlite'

    def __init__(self):
        self.SQLITE_FULL_NAME = os.path.join(self.SQLITE_FILE_DIR, self.SQLITE_FILE_NAME)

    def __str__(self):
        status_dict = {
            'SQLITE_FILE_DIR': self.SQLITE_FILE_DIR,
            'SQLITE_FILE_NAME': self.SQLITE_FILE_NAME,
            'SQLITE_FULL_NAME': self.SQLITE_FULL_NAME,
        }
        return str(status_dict)

act_conf = ActConfig()

#
#
#
import pprint
pp = pprint.PrettyPrinter(indent=4)


def act_info():
    pp.pprint("{} : {}".format("top_work", TOP_WORK))
    pp.pprint("{} : {}".format("top_space", TOP_SPACE))
    pp.pprint(ACT)
    pp.pprint(ACT_CONFIG)


#
#
#
def act_init():
    # OUT Directory
    for tmp_name in ['out_dir', 'log_dir']:
        tmp_dir = ACT_CONFIG[tmp_name]
        pp.pprint(" {} : {} ".format(tmp_name, tmp_dir))
        if os.path.exists(tmp_dir):
            pp.pprint(" directory exists ")
        else:
            os.mkdir(tmp_dir)


#
#
#
import shutil


def act_clear(dir_list):

    # OUT Directory
    for tmp_name in dir_list:
        tmp_dir = ACT_CONFIG[tmp_name]
        pp.pprint(" {} : {} ".format(tmp_name, tmp_dir))
        if not os.path.exists(tmp_dir):
            continue

        print(tmp_name + " (before) : " + str(os.listdir(tmp_dir)))
        shutil.rmtree(tmp_dir)
        os.mkdir(tmp_dir)
        print(tmp_name + " (after) : " + str(os.listdir(tmp_dir)))
        print("\n")


def act_reset():
    act_clear(['out_dir', 'log_dir'] )


def act_clean():
    act_clear(['log_dir'])


#
#
#
ACT_MATCHING = {
    'info': act_info,  # print out information
    'init': act_init,  # create the out directory and the log directory
    'reset': act_reset,  # clear the out directory and the log directory
    'clean': act_clean  # clean the log directory
    }

#
#
#
import sys


if __name__ == "__main__":
    pp.pprint("act-actions")
    if len(sys.argv) == 1:
        pp.pprint(ACT_MATCHING.keys())
    elif len(sys.argv) > 1:
        tmp1 = sys.argv[1]
        ACT_MATCHING[tmp1]()
