
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

websocket = page.js.websocket()
#websocket.connect("localhost", 8765)

page.ui.button("Send").click([
  websocket.connect("localhost", 8765),
  page.js.console.log(websocket.readyState),
  websocket.send("Test"),
  websocket.receive([
    page.js.console.log(websocket.message),
  ]),
])


# page.ui.button("Stop").click([
#   websocket.close()
# ])
#
#
#
# websocket.onerror([
#   page.js.console.log('event', skip_data_convert=True),
# ])
#
# websocket.onmessage([
#   page.js.console.log(websocket.message),
# ])
#
# websocket.onclose([
#   page.js.console.log('event', skip_data_convert=True),
#   websocket.reconnect()
# ])