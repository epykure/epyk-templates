
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

# Create a basic report object
rptObj = Report()
rptObj.body.set_background()

# Input data
data = config.getSeries(5, 40)
data_rest = rptObj.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES, store_location=config.OUTPUT_TEMPS)

ts = rptObj.ui.charts.billboard.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")

g = rptObj.ui.charts.billboard.gauge(60)
p = rptObj.ui.charts.billboard.pie(data, y_column=1, x_axis='g')
d = rptObj.ui.charts.billboard.donut(data, y_column=1, x_axis='g')
s = rptObj.ui.charts.billboard.scatter(data, y_columns=list(range(4)), x_axis='x')
a = rptObj.ui.charts.billboard.line(data, y_columns=list(range(4)), x_axis='x')

r = rptObj.ui.charts.billboard.line_range(data, y_columns=list(range(4)), x_axis='x')

bubble = rptObj.ui.charts.billboard.bubble(data, y_columns=list(range(4)), x_axis='x')
radar = rptObj.ui.charts.billboard.radar(data, y_columns=list(range(4)), x_axis='g')

spline = rptObj.ui.charts.billboard.spline(data, y_columns=list(range(4)), x_axis='x')
step = rptObj.ui.charts.billboard.step(data, y_columns=list(range(4)), x_axis='x')
area = rptObj.ui.charts.billboard.area(data, y_columns=list(range(4)), x_axis='x')
area_step = rptObj.ui.charts.billboard.area_step(data, y_columns=list(range(4)), x_axis='x')

a.axis.x.type = 'categorized'
a.data.names = {'y': 'toto', 'z': 'test'}
a.data.types = {'y': 'bar'}
a.data.selection.multiple = True
a.axis.rotated = True
a.axis.x.show = False
#a.point.show = False
a.point.focus = 200
a.point.select = 200

b = rptObj.ui.charts.billboard.bar(data, y_columns=list(range(4)), x_axis='x')
h = rptObj.ui.charts.billboard.hbar(data, y_columns=list(range(4)), x_axis='g')

#a.zoom.enabled = True
#a.zoom.type = 'drag'

rptObj.ui.grid([
  [r, step],
  [area, spline, radar],
  [g, p, d, bubble],
  [s, a, ts],
  [b, h, area_step]
])

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_charts_billboard"))
