
from epyk.core.Page import Report
from epyk.tests import data_urls

import config


# Create a basic report object
rptObj = Report()

#
data = rptObj.py.requests.csv(data_urls.AIRPORT_TRAFFIC, store_location=config.OUTPUT_TEMPS)

#
rptObj.body.style.css.padding = "0 20px"

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
# rptObj.ui.radio(data, column='city')


#
c1 = rptObj.ui.fields.radio(True, label="Check 1", group_name="group1")
c2 = rptObj.ui.fields.radio(True, label="Check 2", group_name="group1")

c3 = rptObj.ui.inputs.radio(True, label="Check")#

#
c4 = rptObj.ui.icons.tick(False, "Check")

#
c5 = rptObj.ui.lists.radios([
  {"value": True, 'label': 'Python'},
  {"value": False, 'label': 'Javascript'},
])

c1.click([
  c.dom.write(c1.dom.content),
  c.dom.write(c1.dom.selected),
  c.dom.write(c3.dom.val, stringify=True)
])


# Click even
rptObj.ui.button("click").click([
  c.dom.write(c4.dom.val, stringify=True),
  c.dom.write(c5.dom.content),

  # Check the value C1
  c1.js.check()
])

rptObj.ui.button("Uncheck C1").click([
  # uncheck the value C1
  c1.js.uncheck(),
  # Change the label of the tick component
  c4.span.build("New Label"),
  # Change the color CSS property of the internal label
  c4.span.dom.css({"color": 'red'})
])

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_radio"))