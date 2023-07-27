


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
# @pytest.mark.skip()
class TestFlaskMigration:

    MY_UI_DIR='act_ui'
    MY_DB_SQLITE='migrations_db.sqlite'
    MY_DB_DIR='migrations'
    MY_APP_PY='my_app.py'
    

    #@pytest.mark.skip()
    @pytest.mark.order(102)
    def test_flask_migration_m102_config(self, my_config, act_config):
        LOG.info(" my_config ")

        LOG.info(pp.pformat(my_config))
        LOG.info(pp.pformat(act_config))
        #LOG.info(self.MY_WORK_DIR_FULL)
        #LOG.info(self.MY_UI_DIR_FULL)
        LOG.info(str(act_config))
        LOG.info(pp.pformat(str(act_config)))
    

        act_dir_ts=os.path.join(my_config['act_dir'],'act_ts')
        act_dir_ui=os.path.join(my_config['act_dir'],'act_ui')
        LOG.info(act_dir_ts)
        LOG.info(act_dir_ui)

        os.chdir(act_dir_ui)
        tmp_db_sqlite=os.path.join(act_dir_ui,self.MY_DB_SQLITE)
        tmp_db_dir=os.path.join(act_dir_ui,self.MY_DB_DIR)

        if os.path.exists(tmp_db_sqlite):
            LOG.info("Delete:"+tmp_db_sqlite)
            try:
                os.remove(tmp_db_sqlite)
            except OSError:
                LOG.error(tmp_db_sqlite)
                pass
        else:
            LOG.info("Missing:"+tmp_db_sqlite)

        if os.path.exists(tmp_db_dir):
            LOG.info("Delete:"+tmp_db_dir)
            try:
                shutil.rmtree(tmp_db_dir)
            except OSError:
                LOG.error(tmp_db_dir)
                pass
        else:
            LOG.info("Missing:"+tmp_db_dir)

    #@pytest.mark.skip()
    @pytest.mark.order(103)
    def test_flask_migration_m103_run_cmd(self, my_config, act_config):     


        act_dir_ts=os.path.join(my_config['act_dir'],'act_ts')
        act_dir_ui=os.path.join(my_config['act_dir'],'act_ui')
        LOG.info(act_dir_ts)
        LOG.info(act_dir_ui)


        a_cmd='flask db init'
        (o, e, s) = FlaskCli.run_cmd(self.MY_APP_PY, a_cmd, act_dir_ui)
        a_cmd='flask db check'
        (o, e, s) = FlaskCli.run_cmd(self.MY_APP_PY, a_cmd, act_dir_ui)

        a_cmd='flask db migrate'
        (o, e, s) = FlaskCli.run_cmd(self.MY_APP_PY, a_cmd, act_dir_ui)
        a_cmd='flask db check'
        (o, e, s) = FlaskCli.run_cmd(self.MY_APP_PY, a_cmd, act_dir_ui)

        a_cmd='flask db upgrade'
        (o, e, s) = FlaskCli.run_cmd(self.MY_APP_PY, a_cmd, act_dir_ui)
        a_cmd='flask db check'
        (o, e, s) = FlaskCli.run_cmd(self.MY_APP_PY, a_cmd, act_dir_ui)
        #.assertTrue(s == 0)





    #@pytest.mark.skip()
    @pytest.mark.order(104)
    def test_flask_migration_m104_query_user_and_post(self):

        #
        #
        #
        from app import create_app
        app = create_app()
        from app.extensions import db
        from app.models import User, Post
        with app.app_context():
            db.engine.dispose()
            u = User(username='admin')#, email='admin@example.com')
            u.set_password('admin')
            db.session.add(u)
            db.session.commit()

            u = User(username='guest')#, email='john@example.com')
            u.set_password('guest')
            db.session.add(u)
            db.session.commit()

            u1 = User.query.get(1)
            p1 = Post(body='u1 > post1 ', author=u1)
            db.session.add(p1)
            db.session.commit()

            u1 = User.query.get(2)
            p1 = Post(body='u2 > post2 ', author=u1)
            db.session.add(p1)
            db.session.commit()

            u1 = User.query.get(2)
            p1 = Post(body='u2 > post3 ', author=u1)
            db.session.add(p1)
            db.session.commit()

            u1_posts_all = u1.posts.all()
            for p in u1_posts_all:
                LOG.info(" {} {} {} ".format(p.id, p.author.username, p.body))
                LOG.info(" {} {} ".format(u.id, u.username))




    @pytest.mark.skip()
    @pytest.mark.order(105)
    def test_flask_migration_m105_create_user(self):
        from app import create_app
        app = create_app()

        from app.extensions import db
        from app.models import User, Post
        app.app_context().push()

        u = User(username='guest')#, email='john@example.com')
        u.set_password('guest')
        db.session.add(u)
        db.session.commit()

        u1 = User.query.get(1)
        p1 = Post(body='my first post!', author=u1)
        db.session.add(p1)
        db.session.commit()

        u1_posts_all = u1.posts.all()
        for p in u1_posts_all:
            LOG.info(" {} {} {} ".format(p.id, p.author.username, p.body))
            LOG.info(" {} {} ".format(u.id, u.username))

    #@pytest.mark.skip()
    @pytest.mark.order(109)
    def test_flask_migration_m109_query_user_and_post(self):

        from app import create_app
        app = create_app()

        from app.extensions import db
        from app.models import User, Post
        app.app_context().push()

        all_users = User.query.all()
        for u in all_users:
            LOG.info(" {} {} ".format(u.id, u.username))

        all_posts = Post.query.all()
        for p in all_posts:
            LOG.info(" {} {} {} ".format(p.id, p.author.username, p.body))
