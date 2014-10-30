import logging

log = logging.getLogger(__name__)

__version__ = '0.6.0'


try:
    from plex_activity import activity

    # Global objects (using defaults)
    Activity = activity.Activity()
except Exception, ex:
    log.warn('Unable to import submodules - %s', ex)
