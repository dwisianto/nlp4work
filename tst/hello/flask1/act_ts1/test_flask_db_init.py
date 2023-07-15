


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
class TestFlaskDb:

    MY_DB_DIR="./act_ui/my_migrations"

    @pytest.mark.order(11)
    def test_flask_world_core11_help(self, my_config, act_config):
        LOG.info(" my_config ")
        LOG.info(pp.pformat(my_config))
        # LOG.info(pp.pformat(act_config))
        LOG.info(str(act_config))
        LOG.info(pp.pformat(str(act_config)))

    @pytest.mark.order(12)
    def test_flask_client(self):
        from app import create_app

        app = create_app()
        app_tst_client = app.test_client()
        with app.test_client() as c:
            rv = c.get("/index")


    @pytest.mark.skip()
    @pytest.mark.order(12)
    def test_flask_db_init(self):
        #from flask_migrate import init, migrate, upgrade

        #init(directory=self.MY_DB_DIR, multidb=False)
        #migrate(directory=self.MY_DB_DIR)
        #upgrade(directory=self.MY_DB_DIR)
        pass