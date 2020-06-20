
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

data_chart = [
  {1: 10, 'x': 4}
]

button = page.ui.button("test")
scatter = page.ui.charts.nvd3.scatter(data_chart, y_columns=[1], x_axis="x")
bar = page.ui.charts.nvd3.bar(data_chart, y_columns=[1, 2, 3], x_axis="x")
pie = page.ui.charts.nvd3.pie(data_chart, y_columns=[1], x_axis="x")
button.click([
  page.js.post("/data_nv").onSuccess([
      scatter.build(page.js.objects.data['scatter']),
      pie.build(page.js.objects.data['pie']),
      bar.build(page.js.objects.data['bar'])
  ]),
])
