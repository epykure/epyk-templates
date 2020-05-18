import os

from epyk.core.Page import Report


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

data_chart = [
  {1: 10, 'x': 4}
]

button = rptObj.ui.button("test")
scatter = rptObj.ui.charts.nvd3.scatter(data_chart, y_columns=[1], x_axis="x")
bar = rptObj.ui.charts.nvd3.bar(data_chart, y_columns=[1, 2, 3], x_axis="x")
pie = rptObj.ui.charts.nvd3.pie(data_chart, y_columns=[1], x_axis="x")
button.click([
  rptObj.js.post("/data_nv").onSuccess([
      scatter.build(rptObj.js.objects.data['scatter']),
      pie.build(rptObj.js.objects.data['pie']),
      bar.build(rptObj.js.objects.data['bar'])
  ]),
])

rptObj.outs.html_file(path="./../front_end", name=os.path.basename(__file__)[:-3])