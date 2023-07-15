


#
#
#
import pytest
import pprint as pp
import logging
LOG = logging.getLogger(__name__)



#
#
#
import os
import shlex
import shutil
import subprocess


class FlaskCli:
    @staticmethod
    def run_cmd( app, cmd, work_dir):
        """Run a command and return a tuple with (stdout, stderr, exit_code)"""
        os.environ['FLASK_APP'] = app
        #os.environ['DATABASE_URL']='sqlite:////Users/dwyk/d2/s3/m8/ghub/n4wk6/wk_dev_june6/nlp4work/tst/hello/flask1/migrations_db.sqlite'
        
        process = subprocess.Popen(shlex.split(cmd), 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=work_dir)
        (stdout, stderr) = process.communicate()
        LOG.info('\n$ ' + cmd)
        LOG.info(stdout.decode('utf-8'))
        LOG.info(stderr.decode('utf-8'))
        return stdout, stderr, process.wait()



#
#
#
#@pytest.mark.skip()
class TestFlaskMigration:

    MY_UI_DIR='act_ui'
    MY_DB_SQLITE='migrations_db.sqlite'
    MY_DB_DIR='migrations'
    MY_APP_PY='my_app.py'
    
    MY_WORK_DIR_FULL=os.path.dirname(os.path.realpath(__file__))
    MY_UI_DIR_FULL=os.path.join(MY_WORK_DIR_FULL,'..','act_ui')


    #@pytest.mark.skip()
    @pytest.mark.order(102)
    def test_flask_migration_m102_config(self, my_config, act_config):
        LOG.info(" my_config ")
        LOG.info(pp.pformat(my_config))
        # LOG.info(pp.pformat(act_config))
        LOG.info(str(act_config))
        LOG.info(pp.pformat(str(act_config)))
        LOG.info(self.MY_WORK_DIR_FULL)
        LOG.info(self.MY_UI_DIR_FULL)

    # @pytest.mark.skip()
    @pytest.mark.order(103)
    def test_flask_migration_m103_preparation(self, my_config, act_config):     

        os.chdir(self.MY_WORK_DIR)
        tmp_db_sqlite=os.path.join(self.MY_WORK_DIR,self.MY_DB_SQLITE)
        tmp_db_dir=os.path.join(self.MY_WORK_DIR,self.MY_DB_DIR)

        try:
            os.remove(tmp_db_sqlite)
        except OSError:
            LOG.error(tmp_db_sqlite)
            pass

        try:
            shutil.rmtree(tmp_db_dir)
        except OSError:
            LOG.error(tmp_db_dir)
            pass


    #@pytest.mark.skip()
    @pytest.mark.order(104)
    def test_flask_migration_m104_run_cmd(self, my_config, act_config):     
        
        a_cmd='flask db init'
        (o, e, s) = FlaskCli.run_cmd(self.MY_APP_PY, a_cmd, self.MY_UI_DIR_FULL)
        # assertTrue(s == 0)
        a_cmd='flask db check'
        (o, e, s) = FlaskCli.run_cmd(self.MY_APP_PY, a_cmd, self.MY_UI_DIR_FULL)
        # assertTrue(s == 0)

        a_cmd='flask db migrate'
        (o, e, s) = FlaskCli.run_cmd(self.MY_APP_PY, a_cmd, self.MY_UI_DIR_FULL)
        #.assertTrue(s == 0)
        a_cmd='flask db check'
        (o, e, s) = FlaskCli.run_cmd(self.MY_APP_PY, a_cmd, self.MY_UI_DIR_FULL)
        #.assertTrue(s == 0)

        a_cmd='flask db upgrade'
        (o, e, s) = FlaskCli.run_cmd(self.MY_APP_PY, a_cmd, self.MY_UI_DIR_FULL)
        #.assertTrue(s == 0)
        a_cmd='flask db check'
        (o, e, s) = FlaskCli.run_cmd(self.MY_APP_PY, a_cmd, self.MY_UI_DIR_FULL)
        #.assertTrue(s == 0)

    @pytest.mark.order(106)
    def test_flask_migration_m106_admin_user(self):
        from app import create_app
        app = create_app()

        from app.extensions import db
        from app.models import User
        app.app_context().push()

        u = User(username='abc')#, email='john@example.com')
        u.set_password('def')
        db.session.add(u)
        db.session.commit()
        


    @pytest.mark.skip()
    @pytest.mark.order(103)
    def test_flask_migration_m103_preparation(self, my_config, act_config):     

        #def test_migrate_upgrade(self):
        (o, e, s) = self.run_cmd('my_app.py', 'flask db init')
        self.assertTrue(s == 0)
        (o, e, s) = self.run_cmd('app.py', 'flask db check')
        self.assertTrue(s != 0)
        (o, e, s) = self.run_cmd('app.py', 'flask db migrate')
        self.assertTrue(s == 0)
        (o, e, s) = self.run_cmd('app.py', 'flask db check')
        self.assertTrue(s != 0)
        (o, e, s) = self.run_cmd('app.py', 'flask db upgrade')
        self.assertTrue(s == 0)
        (o, e, s) = self.run_cmd('app.py', 'flask db check')
        self.assertTrue(s == 0)

        from .app import app, db, User
        with app.app_context():
            db.engine.dispose()
            db.session.add(User(name='test'))
            db.session.commit()


    @pytest.mark.skip
    @pytest.mark.order(109)
    def test_flask_migration_m109_preparation(self, my_config, act_config):
        LOG.info(" my_config ")
        LOG.info(pp.pformat(my_config))

        os.chdir(self.MY_WORK_DIR)
        tmp_db_sqlite=os.path.join(self.MY_WORK_DIR,self.MY_DB_SQLITE)
        tmp_db_dir=os.path.join(self.MY_WORK_DIR,self.MY_DB_DIR)

        try:
            os.remove(tmp_db_sqlite)
        except OSError:
            pass
        try:
            shutil.rmtree(tmp_db_dir)
        except OSError:
            pass

