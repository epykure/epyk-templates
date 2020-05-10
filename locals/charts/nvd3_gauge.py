
import config

from epyk.core.Page import Report


rptObj = Report()

c = rptObj.ui.charts.nvd3.gauge(42)
#

rptObj.ui.button("reset").click([
  c.build(40),
  #c.js.render(),
])


dataPoints3 = [
  {'label': "mango", 'x': 0, 'y': 20, 'y1': 20, 'r': 10},
  {'label': "grape", 'x': 1, 'y': 18, 'y2': 20, 'r': 5}
]

rptObj.ui.button("reset").click([
  c.build(90),
  #c.js.render(),
])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)