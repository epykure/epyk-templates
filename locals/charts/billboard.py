
from epyk.core.Page import Report

from epyk.tests import data_urls
from epyk.tests import mocks


# Create a basic report object
page = Report()
page.headers.dev() # Change the Epyk logo
page.body.set_background()

# Input data
data = mocks.getSeries(5, 40)
data_rest = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)

ts = page.ui.charts.billboard.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")

g = page.ui.charts.billboard.gauge(60)
p = page.ui.charts.billboard.pie(data, y_columns=[1], x_axis='g')
d = page.ui.charts.billboard.donut(data, y_columns=[1], x_axis='g')
s = page.ui.charts.billboard.scatter(data, y_columns=list(range(4)), x_axis='x')
a = page.ui.charts.billboard.line(data, y_columns=list(range(4)), x_axis='x')

r = page.ui.charts.billboard.line_range(data, y_columns=list(range(4)), x_axis='x')

bubble = page.ui.charts.billboard.bubble(data, y_columns=list(range(4)), x_axis='x')
radar = page.ui.charts.billboard.radar(data, y_columns=list(range(4)), x_axis='g')

spline = page.ui.charts.billboard.spline(data, y_columns=list(range(4)), x_axis='x')
step = page.ui.charts.billboard.step(data, y_columns=list(range(4)), x_axis='x')
area = page.ui.charts.billboard.area(data, y_columns=list(range(4)), x_axis='x')
area_step = page.ui.charts.billboard.area_step(data, y_columns=list(range(4)), x_axis='x')

a.axis.x.type = 'categorized'
a.data.names = {'y': 'toto', 'z': 'test'}
a.data.types = {'y': 'bar'}
a.data.selection.multiple = True
a.axis.rotated = True
a.axis.x.show = False
#a.point.show = False
a.point.focus = 200
a.point.select = 200

b = page.ui.charts.billboard.bar(data, y_columns=list(range(4)), x_axis='x')
h = page.ui.charts.billboard.hbar(data, y_columns=list(range(4)), x_axis='g')

#a.zoom.enabled = True
#a.zoom.type = 'drag'

page.ui.grid([
  [r, step],
  [area, spline, radar],
  [g, p, d, bubble],
  [s, a, ts],
  [b, h, area_step]
])

