
import os

import config

from epyk.core.Page import Report


rptObj = Report()
rptObj.headers.dev()

# Create the server configuration on the JavaScript Side
server = rptObj.data.js.server(config.SERVER_SOCKET_HOST, config.SERVER_SOCKET_PORT).addNamespace('news', alias="name")
socket = rptObj.js.socketio()
socket.connect(from_config=server.getNamespace('name'))

container = rptObj.ui.network.news()
input = rptObj.ui.input()

pie = rptObj.ui.charts.chartJs.polar([], y_columns=[1], x_axis="x")

container.subscribe(socket, 'news received', data=socket.message['content'])
pie.subscribe(socket, 'news received', data=socket.message['pie'])

rptObj.ui.button("Send").click([
  socket.emit("new news", input.dom.content)
])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_INTERACTIVE, name=os.path.basename(__file__)[:-3])