import logging
import traceback

log = logging.getLogger(__name__)

__version__ = '0.6.2'


try:
    from plex_activity import activity

    # Global objects (using defaults)
    Activity = activity.Activity()
except Exception as ex:
    log.warn('Unable to import submodules: %s - %s', ex, traceback.format_exc())
