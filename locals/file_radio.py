
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
rptObj.ui.radio(data, column='city')

#
rptObj.ui.fields.checkbox(True, label="Check")
rptObj.ui.fields.radio(True, label="Check")

#
rptObj.ui.inputs.checkbox(True, label="Check")
rptObj.ui.inputs.radio(True, label="Check")

#
rptObj.ui.icons.tick("Check")

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_radio"))