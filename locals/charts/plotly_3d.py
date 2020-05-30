
import config

from epyk.core.Page import Report
from epyk.tests import data_urls


rptObj = Report()
rptObj.headers.dev()

dataPoints = [
  {'x': 0, 'y': 10, 'y1': 10},
  {'x': 1, 'y': 35, 'y1': 20},
  {'x': 2, 'y': 25, 'y1': 10},
  {'x': 3, 'y': 30, 'y1': 5},
  {'x': 4, 'y': 28, 'y1': 10}]

dataPoints2 = [
  {'label': "mango", 'x1': 0, 'y1': 30, 'z1': 0},
  {'label': "grape", 'x1': 1, 'y1': 28, 'z1': 0}
]

rptObj.ui.hidden("Test")


data_rest = rptObj.py.requests.csv(data_urls.PLOTLY_3D, store_location=config.OUTPUT_TEMPS)

c1 = rptObj.ui._3d.plotly.ribbon(data_rest, y_columns=["y1"], x_axis='x1', z_axis="z1")
c2 = rptObj.ui._3d.plotly.surface(data_rest, y_columns=["y2"], x_axis='x2', z_axis="z2")

rptObj.ui.row([c1, c2])

rptObj.ui.button("reset 1").click([
  c1.build(dataPoints2),
  #c.js.render(),
])

c1.click([
  #rptObj.js.console.log(c.js.value)
])

dataPoints3 = [
  {'label': "mango", 'x': 0, 'y': 20, 'y1': 20, 'r': 10},
  {'label': "grape", 'x': 1, 'y': 18, 'y2': 20, 'r': 5}
]


rptObj.ui.button("reset 2").click([
  c2.build(rptObj.data.plotly.surface(data_rest, y_columns=["y1"], x_axis="x1", z_axis="z1") ),
  #c.js.render(),
])



rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
