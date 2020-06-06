
from epyk.core.Page import Report

# Using data and JavaScript shortcuts
from epyk.core.js import std
from epyk.core.data import events

import config

# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

d = rptObj.ui.div("Test")
d2 = rptObj.ui.div()
d.paste([
  std.alert(events.event.clipboardData.text),
  d2.build(events.data)])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
