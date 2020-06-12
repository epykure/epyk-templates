
import eventlet
import socketio
import config


sio = socketio.Server()
app = socketio.WSGIApp(sio)


@sio.event(namespace='/news')
def connect(sid, environ):
  print('connect ', sid)


@sio.on("file")
def my_message(sid, data):
  print('file ', data)


@sio.on("message", namespace='/news')
def my_message(sid, data):
  print('message ', data)
  sio.emit("chat", data, namespace='/news')


@sio.on("test", namespace='/news')
def test(sid, data):
  sio.emit("this example", {}, room=sid, namespace='/news')
  print('test ', data)


@sio.on("broadcast", namespace='/news')
def broadcast(sid, data):
  """

  :param sid:
  :param data:
  """
  print(data)
  sio.emit("this example", {}, namespace='/news')
  print('test ', data)


@sio.event(namespace='/news')
def disconnect(sid):
  print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen((config.SERVER_SOCKET_HOST, config.SERVER_SOCKET_PORT)), app)
