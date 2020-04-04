
from epyk.core.Page import Report

import config

rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

# Button checkbox
c1 = rptObj.ui.buttons.check(label="C1")

# With some specific CSS Style
c2 = rptObj.ui.buttons.check(True, label="C2")
c3 = rptObj.ui.buttons.check(False, label="C3", icon="fas fa-align-center")

# Based checkbox input component
c4 = rptObj.ui.inputs.checkbox(False).tooltip("C4")

# Field component
c5 = rptObj.ui.fields.checkbox(False, label="C5")

# checks list
data = [{"label": "python", "value": False}, {"label": "Java", "value": 5}]
checks = rptObj.ui.lists.checklist(data)

c2.click([
  # Write the full details of C2
  c.write(c2.dom.val, stringify=True)
], [
  # Check another checkbox
  c3.js.checked()
])

rptObj.ui.button("click").click([
  # Change the label
  c2.label.build("Ok"),
  c3.js.unchecked(),

  # Write the content of the checkbox in C5
  c.write(c5.input.dom.content),

  # Write the content and details of C4
  c.write(c4.dom.content),
  c.write(c4.dom.val, stringify=True)
])

rptObj.ui.button("Check c3").click([
  c3.js.checked()
])


print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_checkbox"))

