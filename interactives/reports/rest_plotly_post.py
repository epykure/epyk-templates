
import os

import config
from epyk.core.Page import Report


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

data_chart = [
  {1: 10, 'x': 4}
]

button = rptObj.ui.button("test")
scatter = rptObj.ui.charts.plotly.bubble(data_chart, y_columns=[1], x_axis="x")
bar = rptObj.ui.charts.plotly.bar(data_chart, y_columns=[1], x_axis="x")
pie = rptObj.ui.charts.plotly.pie(data_chart, y_columns=[1], x_axis="x")
button.click([
  rptObj.js.post("/data_plotly").onSuccess([
      scatter.build(rptObj.js.objects.data['scatter']),
      pie.build(rptObj.js.objects.data['pie']),
      bar.build(rptObj.js.objects.data['bar'])
  ]),
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_INTERACTIVE, name=os.path.basename(__file__)[:-3])