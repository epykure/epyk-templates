
from epyk.core.Page import Report
from epyk.core.data import events

import config

# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

rows = []
for i in range(10):
  row = [rptObj.ui.div("Test %s col %s" % (i, j)).css({"margin": '10px'}) for j in range(3)]
  rows.append(row)

grid = rptObj.ui.layouts.table(rows)
sortable = grid.body.sortable(propagate_only=True)

#sortable.options.ghostClass = "sortable-ghost"
#sortable.options.handle = ".col"

div = rptObj.ui.div("Test")
div.drop([
  div.build(events.data)
])



rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
