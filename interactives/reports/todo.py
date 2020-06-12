
import os

import config

from epyk.core.Page import Report


rptObj = Report()
rptObj.headers.dev()

# Create the server configuration on the JavaScript Side
server = rptObj.data.js.server(config.SERVER_SOCKET_HOST, config.SERVER_SOCKET_PORT).endPoints(["add", "get"]).addNamespace('news', alias="name")

socket = rptObj.js.socketio()
socket.connect(from_config=server.getNamespace('name'))

input = rptObj.ui.input()
input.click([
  socket.emit("test", input.dom.content)
])

comments = rptObj.ui.network.comments("comment_example")
comments.send(socket)
comments.subscribe(socket, 'chat')

danger = rptObj.ui.network.danger()
danger.subscribe(socket, 'chat')

room = rptObj.ui.network.room()

chat = rptObj.ui.network.chat("chat_example")

chat.send(socket)
chat.subscribe(socket, 'chat')

side = rptObj.ui.navigation.side([chat], anchor=room)

socket.on("this example", [
  rptObj.js.console.log("Test"),
  room.js.typing()
])

button = rptObj.ui.button("Click")
button.click([
  socket.emit("broadcast", input.dom.content)
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_INTERACTIVE, name=os.path.basename(__file__)[:-3])
