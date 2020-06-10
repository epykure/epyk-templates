
import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event(namespace='/news')
def connect(sid, environ):
    print('connect ', sid)

@sio.event(namespace='/news')
def my_message(sid, data):
    print('message ', data)

@sio.event(namespace='/news')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app)