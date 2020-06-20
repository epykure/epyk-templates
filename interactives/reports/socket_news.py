
import config

from epyk.core.Page import Report


page = Report()
page.headers.dev()

# Create the server configuration on the JavaScript Side
server = page.data.js.server(config.SERVER_SOCKET_HOST, config.SERVER_SOCKET_PORT).addNamespace('news', alias="name")
socket = page.js.socketio()
socket.connect(from_config=server.getNamespace('name'))

container = page.ui.network.news()
input = page.ui.input()

pie = page.ui.charts.chartJs.polar([], y_columns=[1], x_axis="x")

container.subscribe(socket, 'news received', data=socket.message['content'])
pie.subscribe(socket, 'news received', data=socket.message['pie'])

page.ui.button("Send").click([
  socket.emit("new news", input.dom.content)
])
