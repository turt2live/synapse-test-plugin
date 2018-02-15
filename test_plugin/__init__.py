import logging


class TestPlugin(object):
    def __init__(self, config, api):
        self._config = config
        self._api = api

    def on_room_directory_association_created(self, event):
        logging.info("A room alias was associated with a room", event)
