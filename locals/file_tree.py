
from epyk.core.Page import Report

import config

rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
data = [{"label": 'test', 'items': [{"label": 'child 1', 'color': 'red'}]}]
rptObj.ui.lists.tree(data)

#
rptObj.ui.button("click").click([

])

c.move()

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_tree"))
