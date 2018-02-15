import logging


logger = logging.getLogger(__name__)


class TestPlugin(object):
    def __init__(self, config, api):
        self._config = config
        self._api = api

    def on_room_directory_association_created(self, event):
        logger.info("Room alias created: %r", event)

    @staticmethod
    def parse_config(config):
        return config
