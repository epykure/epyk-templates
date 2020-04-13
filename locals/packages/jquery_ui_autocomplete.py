
from epyk.core.Page import Report

import config

rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
field = rptObj.ui.fields.autocomplete(label="Label")

#
text = rptObj.ui.inputs.autocomplete()
text.options.source = ["abs"]

#
rptObj.ui.button("click").click([
  c.dom.write(field.input.dom.content)
])

#
rptObj.ui.button("Empty").click([
  field.input.dom.empty(),
  text.dom.empty(),
])

c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
