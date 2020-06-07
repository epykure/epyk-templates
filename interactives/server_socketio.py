import socketio
from fastapi import FastAPI


app = FastAPI(debug=True)
sio = socketio.AsyncServer(async_mode='asgi')
sio_asgi_app = socketio.ASGIApp(sio, app, socketio_path="/api/socket.io")

class ConnectNS(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        logging.debug("Websocket connected %s", sid)

    def on_disconnect(self, sid):
        logging.debug("Websocket disconnected %s" % sid)
		
sio.register_namespace(ConnectNS('/'))