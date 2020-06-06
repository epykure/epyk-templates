
from epyk.core.Page import Report
from epyk.core.js import std

import config

# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

div = rptObj.ui.div("Test")
div.onReady([
  # Create a bespoke type of event
  div.dom.addEventListener("build", std.alert("Ok"))
])

div2 = rptObj.ui.div("Trigger Event")
div2.click([
  # Iitiate the event
  std.createEvent('test_event'),
  std.initEvent("build", 'test_event', True, True),

  # Dispatch this event to trigger the component div
  div2.dom.dispatchEvent(std.getEvent('test_event'))
])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
