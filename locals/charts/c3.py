
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

# Create a basic report object
rptObj = Report()
rptObj.body.set_background()

data = config.getSeries(5, 40)

data_rest = rptObj.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES, store_location=config.OUTPUT_TEMPS)

ts = rptObj.ui.charts.c3.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")

g = rptObj.ui.charts.c3.gauge(60)
p = rptObj.ui.charts.c3.pie(data, y_column=1, x_axis='g')
d = rptObj.ui.charts.c3.donut(data, y_column=1, x_axis='g')
s = rptObj.ui.charts.c3.scatter(data, y_columns=list(range(4)), x_axis='x')

#stanford = rptObj.ui.charts.c3.stanford(data, y_columns=list(range(4)), x_axis='x', epoch_col=0)

spline = rptObj.ui.charts.c3.spline(data, y_columns=list(range(4)), x_axis='x')
step = rptObj.ui.charts.c3.step(data, y_columns=list(range(4)), x_axis='x')
area = rptObj.ui.charts.c3.area(data, y_columns=list(range(4)), x_axis='x')
area_step = rptObj.ui.charts.c3.area_step(data, y_columns=list(range(4)), x_axis='x')

# a.axis.x.type = 'categorized'
# a.data.names = {'y': 'toto', 'z': 'test'}
# a.data.types = {'y': 'bar'}
# a.data.selection.multiple = True
# a.axis.rotated = True
# a.axis.x.show = False
# #a.point.show = False
# a.point.focus = 200
# a.point.select = 200

b = rptObj.ui.charts.c3.bar(data, y_columns=list(range(4)), x_axis='x')
h = rptObj.ui.charts.c3.hbar(data, y_columns=list(range(4)), x_axis='g')

#a.zoom.enabled = True
#a.zoom.type = 'drag'

rptObj.ui.grid([
  [g, p, d, spline],
  [s, ts, step],
  [b, h, area, area_step]
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
