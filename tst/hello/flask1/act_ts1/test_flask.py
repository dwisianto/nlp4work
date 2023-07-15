


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
@pytest.mark.skip()
class TestFlaskBasic:

    @pytest.mark.skip()
    @pytest.mark.order(11)
    def test_flask_world_core11_help(self, my_config, act_config):
        LOG.info(" my_config ")
        LOG.info(pp.pformat(my_config))
        # LOG.info(pp.pformat(act_config))
        LOG.info(str(act_config))
        LOG.info(pp.pformat(str(act_config)))

    @pytest.mark.skip()
    @pytest.mark.order(12)
    def test_flask_request_login(self):
        import requests
        r = requests.get("http://localhost:5000")
        LOG.info( r.status_code )

    @pytest.mark.skip()
    @pytest.mark.order(12)
    def test_flask_client(self):
        from app import create_app

        app = create_app()
        app_tst_client = app.test_client()
        with app.test_client() as c:
            rv = c.get("/index")

    @pytest.mark.skip()
    @pytest.mark.order(13)
    def test_flask_index(self):
        from app import create_app
        app = create_app()

        from app.extensions import db
        from app.models import User
        app.app_context().push()

        u = User(username='asdf')#, email='john@example.com')
        u.set_password('asdf')
        db.session.add(u)
        db.session.commit()

    @pytest.mark.skip()
    @pytest.mark.order(302)
    def test_flask_clean_up(self):
        from app import create_app
        app = create_app()

        from app.extensions import db
        from app.models import User
        app.app_context().push()

        #from flask_migrate import init, migrate, upgrade
        #init(directory=self.MY_DB_DIR, multidb=False)
        #migrate(directory=self.MY_DB_DIR)
        #upgrade(directory=self.MY_DB_DIR)


        #u = User(username='john')#, email='john@example.com')
        #db.session.add(u)
        #db.session.commit()


        users = User.query.all()
        for u in users:
            db.session.delete(u)

        #posts = Post.query.all()
        #for p in posts:
        #    db.session.delete(p)

        db.session.commit()

        


@pytest.mark.skip()
class TestFlaskDbMigration:

    MY_DB_SQLITE='./act_ui/my_db.sqlite'
    MY_DB_DIR="./act_ui/migrations"    

    #@pytest.mark.skip()
    @pytest.mark.order(301)
    def test_flask_db_migrate_setup(self):
        import os
        try:
            os.remove(self.MY_DB_SQLITE)
        except OSError as oserror:
            print(str(oserror))

        import shutil
        try:
            shutil.rmtree(self.MY_DB_DIR) 
        except OSError as e:
            print(str(e))
        

    @pytest.mark.skip()
    @pytest.mark.order(302)
    def test_flask_db_migrate_routine(self):
        from app import create_app
        app = create_app()
        app.app_context().push()


        from app.extensions import db
        from app.models import User

        u = User(username='abc')#, email='john@example.com')
        u.set_password('def')
        db.session.add(u)
        db.session.commit()

        from flask_migrate import init, migrate, upgrade
        init(directory=self.MY_DB_DIR, multidb=False)
        migrate(directory=self.MY_DB_DIR)



    @pytest.mark.skip()
    @pytest.mark.order(303)
    def test_flask_db_migrate_users(self):
        from app import create_app
        app = create_app()
        app.app_context().push()



    #@pytest.mark.skip()
    @pytest.mark.order(304)
    def test_flask_db_migrate_upgrade(self):
        from app import create_app
        app = create_app()
        app.app_context().push()

        from flask_migrate import init, migrate, upgrade
        #init(directory=self.MY_DB_DIR, multidb=False)
        #migrate(directory=self.MY_DB_DIR)
        #upgrade(directory=self.MY_DB_DIR)
