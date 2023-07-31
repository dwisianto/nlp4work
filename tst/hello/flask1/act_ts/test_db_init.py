
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



# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-unit-testing-legacy
class TestDbInit:

    @pytest.mark.order(1)
    def test_db_init_i1_config(self, act_config):
        LOG.info(" act_config ")
        LOG.info(pp.pformat(str(act_config)))
        LOG.info(act_config.act_ts)
        LOG.info(act_config.act_ui)

        LOG.info(os.getenv('MY_DATA'))
        LOG.info(os.getenv('MY_DAT'))
        LOG.info(os.getenv('DATABASE_URL'))
        LOG.info(os.getenv('FLASK_ENV'))
        LOG.info(os.getenv('FLASK_APP'))
        LOG.info(os.getenv('SECRET_KEY'))


    @pytest.mark.order(2)
    def test_db_init_i2_clean_up(self, act_config):

        tmp_db_sqlite = act_config.act_ui_db_file
        if os.path.exists(tmp_db_sqlite):
            LOG.info("Delete:"+tmp_db_sqlite)
            try:
                os.remove(tmp_db_sqlite)
            except OSError:
                LOG.error(tmp_db_sqlite)
                pass
        else:
            LOG.info("Missing:"+tmp_db_sqlite)

        tmp_db_dir = act_config.act_ui_db_dir
        if os.path.exists(tmp_db_dir):
            LOG.info("Delete:"+tmp_db_dir)
            try:
                shutil.rmtree(tmp_db_dir)
            except OSError:
                LOG.error(tmp_db_dir)
                pass
        else:
            LOG.info("Missing:"+tmp_db_dir)


    # @pytest.mark.skip
    @pytest.mark.order(3)
    def test_db_init_i3_user_admin(self, act_config):

        from app import create_app
        app_tst = create_app() # create_app().test_client
        #app_tst.config['TESTING'] = True
        #app_tst.config['WTF_CSRF_ENABLED'] = False
        #app_tst.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        #app_tst.config['DATABASE_URL'] = ''

        from app.extensions import db
        from app.models import User, Post


        app_tst.app_context().push()
        db.create_all()

        u = User(username='admin')#, email='john@example.com')
        u.set_password('admin')
        db.session.add(u)
        db.session.commit()

        u1 = User.query.get(1)
        p1 = Post(body='admin: first post!', author=u1)
        db.session.add(p1)
        db.session.commit()

        u1 = User.query.get(1)
        p1 = Post(body='admin: second post!', author=u1)
        db.session.add(p1)
        db.session.commit()



    #@pytest.mark.skip
    @pytest.mark.order(4)
    def test_db_init_i4_user_guest(self, act_config):

        from app import create_app
        app_tst = create_app() # create_app().test_client
        #app_tst.config['TESTING'] = True
        #app_tst.config['WTF_CSRF_ENABLED'] = False
        #app_tst.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        #app_tst.config['DATABASE_URL'] = ''

        from app.extensions import db
        from app.models import User, Post


        app_tst.app_context().push()
        db.create_all()


        u = User(username='guest')#, email='john@example.com')
        u.set_password('guest')
        db.session.add(u)
        db.session.commit()

        u1 = User.query.get(1)
        p1 = Post(body='guest: first post!', author=u1)
        db.session.add(p1)
        db.session.commit()

    #@pytest.mark.skip
    @pytest.mark.order(5)
    def test_db_init_i5_user_friend(self, act_config):

        from app import create_app
        app_tst = create_app() # create_app().test_client
        #app_tst.config['TESTING'] = True
        #app_tst.config['WTF_CSRF_ENABLED'] = False
        #app_tst.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        #app_tst.config['DATABASE_URL'] = ''

        from app.extensions import db
        from app.models import User, Post


        app_tst.app_context().push()
        db.create_all()


        u = User(username='friend')#, email='john@example.com')
        u.set_password('friend')
        db.session.add(u)
        db.session.commit()

        u1 = User.query.get(1)
        p1 = Post(body='friend: first post!', author=u1)
        db.session.add(p1)
        db.session.commit()

        u1 = User.query.get(1)
        p1 = Post(body='friend: second post!', author=u1)
        db.session.add(p1)
        db.session.commit()


    # @pytest.mark.skip
    @pytest.mark.order(9)
    def test_db_init_i9_setup(self, act_config):

        #
        #
        #
        from app import create_app
        app = create_app()
        from app.extensions import db
        from app.models import User, Post
        with app.app_context():
            db.engine.dispose()
            u = User(username='admin9')#, email='admin@example.com')
            u.set_password('admin9')
            db.session.add(u)
            db.session.commit()

            u = User(username='guest9')#, email='john@example.com')
            u.set_password('guest9')
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

            u1 = User.query.get(3)
            p1 = Post(body='u2 > post3 ', author=u1)
            db.session.add(p1)
            db.session.commit()

            u1_posts_all = u1.posts.all()
            for p in u1_posts_all:
                LOG.info(" {} {} {} ".format(p.id, p.author.username, p.body))
                LOG.info(" {} {} ".format(u.id, u.username))


            u1_posts_all = u1.posts.all()
            for p in u1_posts_all:
                LOG.info(" {} {} {} ".format(p.id, p.author.username, p.body))
                LOG.info(" {} {} ".format(u.id, u.username))
