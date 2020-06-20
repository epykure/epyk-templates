
import config

from epyk.core.Page import Report


page = Report()
page.headers.dev()

# Create the server configuration on the JavaScript Side
server = page.data.js.server(config.SERVER_SOCKET_HOST, config.SERVER_SOCKET_PORT).endPoints(["add", "get"]).addNamespace('news', alias="name")

socket = page.js.socketio()
socket.connect(from_config=server.getNamespace('name'))

input = page.ui.input()
input.click([
  socket.emit("test", input.dom.content)
])

days = page.ui.fields.days()
years = page.ui.fields.years()
months = page.ui.fields.months()
page.ui.fields.weeks()
comments = page.ui.network.comments("comment_example")
comments.send(socket)
comments.subscribe(socket, 'chat')

danger = page.ui.network.danger()
danger.subscribe(socket, 'chat')

room = page.ui.network.room("")

chat = page.ui.network.chat("chat_example")

chat.send(socket)
chat.subscribe(socket, 'chat')

side = page.ui.navigation.side([chat], anchor=room)

socket.on("this example", [
  page.js.console.log("Test"),
  room.js.typing()
])

button = page.ui.button("Click")
button.click([
  #socket.emit("broadcast", input.dom.content),
  page.js.console.log(months.dom.content)
])

