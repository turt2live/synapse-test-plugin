class TestPlugin(object):
    def __init__(self, config, api):
        self._config = config
        self._api = api

    def on_room_directory_association_created(self, event):
        self._api.hs.get_event_creation_handler().create_and_send_nonmember_event(
            event['creator'],
            {
                "type": "m.room.message",
                "room_id": event['room_id'],
                "sender": event['creator'],
                "content": {
                    "msgtype": "m.notice",
                    "body": "[Test Plugin] Alias " + event['room_alias'].to_string() + " created on this room",
                }
            }
        )

    @staticmethod
    def parse_config(config):
        return config
