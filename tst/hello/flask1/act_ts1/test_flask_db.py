
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

    @pytest.mark.order(11)
    def test_flask_db_config11_help(self, my_config, act_config):
        LOG.info(" my_config ")
        LOG.info(pp.pformat(my_config))
        # LOG.info(pp.pformat(act_config))
        LOG.info(str(act_config))
        LOG.info(pp.pformat(str(act_config)))

    @pytest.mark.order(12)
    def test_flask_db_config11_init(self, my_config, act_config):
        LOG.info(" my_config ")
        LOG.info(pp.pformat(my_config))
        # LOG.info(pp.pformat(act_config))
        LOG.info(str(act_config))
        LOG.info(pp.pformat(str(act_config)))

