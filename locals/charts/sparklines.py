
from epyk.core.Page import Report
import config

# Create a basic report object
rptObj = Report()

rptObj.ui.charts.sparkline("box", [1, 2, 3, 4, 5, 4, 3, 2, 1])
l = rptObj.ui.charts.sparkline("line", [1, 2, 3, 4, 5, 4, 3, 2, 10])
l.click([
  rptObj.js.console.log(l.dom.val),
  rptObj.js.console.log(l.dom.content),
  rptObj.js.console.log(l.dom.offset),
])

s = rptObj.ui.charts.sparkline("bar", [1, 2, 3], title="Top Clients (#)",  options={"barWidth": 20})
s.hover([
  rptObj.js.console.log(s.dom.val),
  rptObj.js.console.log(s.dom.content),
  rptObj.js.console.log(s.dom.offset),
])
rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
