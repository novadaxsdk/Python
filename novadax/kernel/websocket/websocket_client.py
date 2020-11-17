import socketio


class BaseWebSocketClient:

    def __init__(self, endpoint):
        self._endpoint = endpoint
        self._socket = None

    def get_socket(self):
        if self._socket is None:
            print(self._endpoint)
            self._socket = socketio.Client()
            self._socket.connect(self._endpoint, transports=['websocket'])
        return self._socket

    def subscribe(self, topic, callback):
        self.get_socket().emit("SUBSCRIBE", [topic])
        self.get_socket().on(topic, callback)

    def unsubscribe(self, topic):
        self.get_socket().emit("UNSUBSCRIBE", [topic])
