
import os

import config

from epyk.core.Page import Report


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

# Create the server configuration on the JavaScript Side
server = rptObj.data.js.server(config.SERVER_SOCKET_HOST, config.SERVER_SOCKET_PORT).addNamespace('test', alias="name")
socket = rptObj.js.socketio()
socket.connect(from_config=server.getNamespace('name'))

socket.on('my response', [
  rptObj.js.console.log("Ok")
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