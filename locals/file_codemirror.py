
from epyk.core.Page import Report

import config

rptObj = Report()

# Console component
console = rptObj.ui.rich.console("This is a log section for all the events in the different buttons *", options={"timestamp": True})


console.move()

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_codemirror"))
