import socketio
import logging
import os
import sys

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI(debug=True)
sio = socketio.AsyncServer(async_mode='asgi')
sio_asgi_app = socketio.ASGIApp(sio, app, socketio_path="/api/socket.io")

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cur_dir, "..", "..", "epyk-ui"))


@app.get('/', response_class=HTMLResponse)
def home():
  """
  Report creation on the fly in Flask
  """
  from epyk.core.Page import Report

  rptObj = Report()
  list = rptObj.ui.list()
  for pyfile in os.listdir("reports"):
    list.add_item(rptObj.ui.link(pyfile, url="/report/%s" % pyfile[:-3]).css({"padding": '2px 0', 'display': 'block'}))
  return rptObj.outs.html()


@app.get("/report/{file_name}", response_class=HTMLResponse)
def read_item(file_name):
  html_content = open(os.path.join('front_end', '%s.html' % file_name)).read()
  return html_content


class ConnectNS(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        logging.debug("Websocket connected %s", sid)

    def on_disconnect(self, sid):
        logging.debug("Websocket disconnected %s" % sid)


sio.register_namespace(ConnectNS('/'))