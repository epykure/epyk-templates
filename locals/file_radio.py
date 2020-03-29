
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
c = rptObj.ui.fields.checkbox(True, label="Check")
c.click([
  rptObj.js.console.log(c.dom.content)
])

r = rptObj.ui.fields.radio(True, label="Check 1", group_name="group1")
r1 = rptObj.ui.fields.radio(True, label="Check 2", group_name="group1")

r.click([
  rptObj.js.console.log(r.dom.content)
])

#
rptObj.ui.inputs.checkbox(True, label="Check")
rptObj.ui.inputs.radio(True, label="Check")

#
rptObj.ui.icons.tick(False, "Check")


rptObj.ui.lists.radios([
  {"value": True, 'label': 'Python'},
  {"value": False, 'label': 'Javascript'},
])


data = [{"label": "python", "value": False}, {"label": "Java", "value": 5}]
checks = rptObj.ui.lists.checklist(data)


print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_radio"))