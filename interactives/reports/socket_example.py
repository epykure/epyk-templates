
import os

import config

from epyk.core.Page import Report


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

socket = rptObj.js.socketio()
socket.connect(url="http://127.0.0.1", port=5010, namespace='test')

rptObj.body.onReady([
  socket.on('my response', [
    rptObj.js.console.log("Ok")
  ])
])

#
input = rptObj.ui.input()


rptObj.ui.div()

rptObj.ui.button("Send").click([
  socket.send(input.dom.content)
])


rptObj.ui.button("Response").click([
  socket.emit("my event")
])


rptObj.ui.button("Broadcast").click([
  socket.emit("my broadcast event")
])

#
rptObj.ui.button("Disconnect").click([
  socket.emit("disconnect")
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_INTERACTIVE, name=os.path.basename(__file__)[:-3])