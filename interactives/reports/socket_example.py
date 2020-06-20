
import config

from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

# Create the server configuration on the JavaScript Side
server = page.data.js.server(config.SERVER_SOCKET_HOST, config.SERVER_SOCKET_PORT).addNamespace('test', alias="name")
socket = page.js.socketio()
socket.connect(from_config=server.getNamespace('name'))

socket.on('my response', [
  page.js.console.log("Ok")
])

#
input = page.ui.input()


page.ui.div()

page.ui.button("Send").click([
  socket.send(input.dom.content)
])


page.ui.button("Response").click([
  socket.emit("my event")
])


page.ui.button("Broadcast").click([
  socket.emit("my broadcast event")
])

#
page.ui.button("Disconnect").click([
  socket.emit("disconnect")
])
