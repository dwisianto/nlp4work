
from act.hello_world_class import HelloWorldClass, HelloWorldSubClass

#
#
#
import os
import pytest
import logging
LOG = logging.getLogger(__name__)


#
#
#
@pytest.mark.skip()
class TestHelloWorldIO:

    @pytest.mark.order(11)
    def test_hello_world_io11_help(self, my_config):
        LOG.info(" my_config ")
        LOG.info(my_config)

        LOG.info(os.environ['JAVA_HOME'])

        LOG.info(HelloWorldClass())
        LOG.info(HelloWorldSubClass())

    @pytest.mark.order(12)
    @pytest.mark.parametrize("num,output", [('a', 'bcd'), ('e', 'fgh')])
    def test_hello_world_io11_param(self, num, output):
        LOG.info(" my_config ")
        LOG.info(num)
        LOG.info(output)


#
#
#
@pytest.mark.skip()
@pytest.mark.order(after="TestHelloWorldIO")
class TestHelloWorldIOExport:

    @pytest.mark.order(21)
    def test_hello_world_io21_export_help(self, my_config):
        my_argv = list()
        my_argv.append("--config")
        my_argv.append(str(my_config["act_dir"]))
        my_argv.append("--workflow")
        my_argv.append("create_and_export")
        LOG.info(my_argv)


#
#
#
@pytest.mark.skip()
@pytest.mark.order(after="TestHelloWorldIOImport")
class TestHelloWorldIOImport:

    @pytest.mark.order(31)
    def test_hello_world_io31_import_help(self, my_config):
        LOG.info(my_config)
