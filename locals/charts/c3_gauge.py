
import config

from epyk.core.Page import Report


rptObj = Report()

dataPoints = [
  {'x': 0, 'y': 10, 'y1': 10},
  {'x': 1, 'y': 35, 'y1': 20},
  {'x': 2, 'y': 25, 'y1': 10},
  {'x': 3, 'y': 30, 'y1': 5},
  {'x': 4, 'y': 28, 'y1': 10}]

dataPoints2 = [
  {'label': "mango", 'x': 0, 'y': 30, 'y1': 0},
  {'label': "grape", 'x': 1, 'y': 28, 'y1': 0}
]

rptObj.ui.hidden("Test")

c = rptObj.ui.charts.c3.gauge(45)
#c.label(0, "Test")

rptObj.ui.button("reset").click([
  c.build(90) #dataPoints2),
  #c.js.render(),
])

c.click([
  rptObj.js.console.log(c.js.content)
])

dataPoints3 = [
  {'label': "mango", 'x': 0, 'y': 20, 'y1': 20, 'r': 10},
  {'label': "grape", 'x': 1, 'y': 18, 'y2': 20, 'r': 5}
]

rptObj.ui.button("reset").click([
  c.build(10),
  #c.js.render(),
])



rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
