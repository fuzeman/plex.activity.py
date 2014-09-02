from plex_activity.sources.base import Source

import json
import logging
import websocket

log = logging.getLogger(__name__)


class WebSocket(Source):
    name = 'websocket'
    events = [
        'notification.playing',
        'notification.progress',
        'notification.status'
    ]

    opcode_data = (websocket.ABNF.OPCODE_TEXT, websocket.ABNF.OPCODE_BINARY)

    def __init__(self, activity):
        super(WebSocket, self).__init__()

        self.ws = None
        self.reconnects = 0

        # Pipe events to the main activity instance
        self.pipe(self.events, activity)

    def connect(self):
        self.ws = websocket.create_connection('ws://127.0.0.1:32400/:/websockets/notifications')

        log.info('Connected to notification websocket')

    def run(self):
        self.connect()

        log.debug('Ready')

        while True:
            try:
                self.process(*self.receive())

                # successfully received data, reset reconnects counter
                self.reconnects = 0
            except websocket.WebSocketConnectionClosedException:
                if self.reconnects <= 5:
                    self.reconnects += 1

                    # Increasing sleep interval between reconnections
                    if self.reconnects > 1:
                        time.sleep(2 * (self.reconnects - 1))

                    log.info('WebSocket connection has closed, reconnecting...')
                    self.connect()
                else:
                    log.error('WebSocket connection unavailable, activity monitoring not available')
                    break

    def receive(self):
        frame = self.ws.recv_frame()

        if not frame:
            raise websocket.WebSocketException("Not a valid frame %s" % frame)
        elif frame.opcode in self.opcode_data:
            return frame.opcode, frame.data
        elif frame.opcode == websocket.ABNF.OPCODE_CLOSE:
            self.ws.send_close()
            return frame.opcode, None
        elif frame.opcode == websocket.ABNF.OPCODE_PING:
            self.ws.pong("Hi!")

        return None, None

    def process(self, opcode, data):
        if opcode not in self.opcode_data:
            return False

        try:
            info = json.loads(data)
        except Exception, e:
            log.warn('Error decoding message from websocket: %s' % e)
            log.debug(data)
            return False

        type = info.get('type')

        if not type:
            return False

        # Pre-process message (if function exists)
        process_func = getattr(self, 'process_%s' % type, None)

        if process_func and process_func(info):
            return True

        # Emit raw message
        children = info.get('_children', [])

        if len(children) > 1:
            self.emit('notification.%s' % type, children)
        elif len(children) == 1:
            self.emit('notification.%s' % type, children[0])
        else:
            self.emit('notification.%s' % type, info)

        return True
