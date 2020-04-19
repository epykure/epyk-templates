
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

current = rptObj.ui.menus.selections([])

#
modal = rptObj.ui.modals.dialog("rsr")
modal.options.title = "Test Modal"

#
input = rptObj.ui.input("")
input_hide = rptObj.ui.inputs.hidden("Hidden text")

#
rptObj.ui.button("click").click([
  modal.build(input_hide.dom.content),
  modal.js.open()
])

c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
