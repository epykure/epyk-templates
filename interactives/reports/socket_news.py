
import os

import config

from epyk.core.Page import Report


rptObj = Report()
rptObj.headers.dev()

socket = rptObj.js.socketio()
socket.connect(url="http://127.0.0.1", port=5010, namespace='news')

container = rptObj.ui.network.news()
input = rptObj.ui.input()

pie = rptObj.ui.charts.chartJs.polar([], y_columns=[1], x_axis="x")

container.subscribe(socket, 'news received', data=socket.message['content'])
pie.subscribe(socket, 'news received', data=socket.message['pie'])

rptObj.ui.button("Send").click([
  socket.emit("new news", input.dom.content)
])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_INTERACTIVE, name=os.path.basename(__file__)[:-3])