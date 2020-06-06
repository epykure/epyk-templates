
from epyk.core.Page import Report

# Using data and JavaScript shortcuts
from epyk.core.js import std
from epyk.core.data import events

import config

# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

div = rptObj.ui.div("Test")
div.style.css.background = 'white'

button = rptObj.ui.button("show")
popup = rptObj.ui.layouts.popup([div], options={"background": False, 'draggable': True})

button.click([
  popup.dom.show()
])
rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
