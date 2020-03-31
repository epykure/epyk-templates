
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

current = rptObj.ui.fields.today(label="Date field")


rptObj.ui.button("click").click([

])

c.move()

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_jquery_ui_datepicker"))
