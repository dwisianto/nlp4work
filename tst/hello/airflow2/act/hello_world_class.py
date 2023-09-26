

import logging
LOG = logging.getLogger(__name__)


class HelloWorldClass:

    def __str__(self):
        LOG.info("class representation")
        return "Hello Hello Class"


class HelloWorldSubClass(HelloWorldClass):

    def __str__(self):
        LOG.info("class sub-class")
        return "Hello World SubClass"
