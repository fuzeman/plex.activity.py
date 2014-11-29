import logging
logging.basicConfig(level=logging.DEBUG)

from plex import Plex
from plex_activity import Activity
from plex_metadata import Metadata



if __name__ == '__main__':
    # Set authentication token
    Plex.configuration.defaults.authentication(
        raw_input('Authentication token: ')
    )

    # Bind events
    @Activity.on('websocket.playing')
    def ws_playing(info):
        print "[websocket.playing]", info

    @Activity.on('logging.playing')
    def lo_playing(info):
        print "[logging.playing]", info

    @Activity.on('logging.action.played')
    def on_played(info):
        print "[logging.action.played]", info

        metadata = Metadata.get(info.get('rating_key'))
        print metadata

    @Activity.on('logging.action.unplayed')
    def on_unplayed(info):
        print "[logging.action.unplayed]", info

    Activity.start()
