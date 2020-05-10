
import config

from epyk.core.Page import Report
from epyk.core.data import Jsdata

rptObj = Report()

dataPoints = [
  {'x': 0, 'y': 10, 'y1': 10},
  {'x': 1, 'y': 35, 'y1': 20},
  {'x': 2, 'y': 25, 'y1': 10},
  {'x': 3, 'y': 30, 'y1': 5},
  {'x': 4, 'y': 28, 'y1': 10}]

dataPoints2 = [
  {'label': "mango", 'x': 0, 'y': 30, 'y1': 10},
  {'label': "grape", 'x': 1, 'y': 28, 'y1': 5}
]

rptObj.ui.input("Test")

js_data_object = Jsdata(dataPoints2)

c = rptObj.ui.charts.c3.line(js_data_object, y_columns=["y", 'y1'], x_axis='x') #dataPoints, y_columns=["y", 'y1'], x_axis='x')
#c.label(0, "Test")

rptObj.ui.button("reset").click([
  c.build(dataPoints2),
  #c.js.render(),
])
#
c.click([
  rptObj.js.console.log(c.js.content),
])

dataPoints3 = [
  {'label': "mango", 'x': 0, 'y': 20, 'y1': 20, 'r': 10},
  {'label': "grape", 'x': 1, 'y': 18, 'y2': 20, 'r': 5}
]
print(c.js.load(['test', 1, 15, 26, 89]).toStr())
rptObj.ui.button("add").click([
  c.js.load(['test', 1, 15, 26, 89]),
  #c.js.render(),
])

rptObj.ui.button("remove").click([
  c.js.unload(['test']),
  #c.js.render(),
])


rptObj.ui.button("reset").click([
  c.build(dataPoints3),
  #c.js.render(),
])



rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)