from plex_activity.core.helpers import str_format
from plex_activity.sources.s_logging.parsers.base import Parser, LOG_PATTERN

import re


class ScrobbleParser(Parser):
    pattern = str_format(LOG_PATTERN, message=r'Library item (?P<rating_key>\d+) \'(?P<title>.*?)\' got (?P<action>(?:un)?played) by account (?P<account_key>\d+)!.*?')
    regex = re.compile(pattern, re.IGNORECASE)

    events = [
        'action.scrobble'
    ]

    def __init__(self, main):
        super(ScrobbleParser, self).__init__(main)

        # Pipe events to the main logging activity instance
        self.pipe(self.events, main)

    def process(self, line):
        match = self.regex.match(line)
        if not match:
            return False

        self.emit('action.scrobble', {
            'account_key': match.group('account_key'),
            'rating_key': match.group('rating_key'),

            'title': match.group('title'),
            'action': match.group('action'),
        })

        return True
