
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



from werkzeug.security import generate_password_hash


#
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-unit-testing-legacy
#
#@pytest.mark.skip
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

        LOG.info(os.getenv('SEED_XLSX'))
        LOG.info(os.getenv('SEED_XLSX_FULL_PATH'))


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
    @pytest.mark.parametrize("user_name,user_pass",
                             [('sme', 'sme'),
                              ('expert', 'expert'),
                              ('guest', 'guest'),
                              ('friend', 'friend'),
                              ])
    def test_db_init_i3_user_admin(self, act_config, act_faker, user_name, user_pass):

        from datetime import datetime

        from app import create_app
        app_tst = create_app() # create_app().test_client

        from app.extensions import db
        from app.models import User, Tale

        app_tst.app_context().push()
        db.create_all()

        u = User(username=user_name,
                password_hash = generate_password_hash(user_pass))
        db.session.add(u)
        db.session.commit()

        # Tales
        u0 = User.query.filter_by(username=u.username).first_or_404()
        for i in range(act_config.tale_num_of_narrative):
            t0 = Tale(tale_narrative=act_faker.text(),
                      tale_narrative_id=act_faker.random_int(),
                      tale_narrative_correctness="no",
                      tale_narrative_submission_date=act_faker.date_time_between(start_date='-1y',end_date='now'),
                      author=u0)
            db.session.add(t0)
            db.session.commit()


@pytest.mark.order(after="TestDbInit")
class TestDbInitSummary:

    # @pytest.mark.skip
    @pytest.mark.order(1)
    def test_db_init_faker_f1_config(self, act_config):

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


    @pytest.mark.order(9)
    def test_db_init_i9_user_query_all(self, act_config):

        from app import create_app
        app = create_app()
        from app.extensions import db
        from app.models import User, Tale
        with app.app_context():
            db.engine.dispose()

            for t in Tale.query.all():
                LOG.info(" {} {} {} {} {} ".format( t.tale_id,
                                                    t.tale_narrative_id,
                                                    t.tale_narrative,
                                                    t.user_id,
                                                    t.author.username))

            for u in User.query.all():
                LOG.info(str(u))
                LOG.info(" {} {} ".format(u.id, u.username))

# Notes
#
# 2023-08-02
#
#        app_tst = create_app() # create_app().test_client
#        #app_tst.config['TESTING'] = True
#        #app_tst.config['WTF_CSRF_ENABLED'] = False
#        #app_tst.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
#        #app_tst.config['DATABASE_URL'] = ''
