
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

# Create a basic report object
rptObj = Report()
rptObj.body.set_background()

# Input data
data = config.getSeries(5, 30)
data_rest = rptObj.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES, store_location=config.OUTPUT_TEMPS)

ts = rptObj.ui.charts.chartJs.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")
#ts.hover([
#  rptObj.js.console.log(ts.js.value, skip_data_convert=True)
#])
yaxis = ts.options.scales.add_y_axis()
yaxis.gridLines.display = True
yaxis.gridLines.color = 'red'
yaxis.gridLines.zeroLineWidth = 1
yaxis.gridLines.zeroLineColor = 'red'
yaxis.gridLines.drawBorder = True
yaxis.ticks.fontColor = 'red'
yaxis.ticks.beginAtZero = True
yaxis.add_label('Y Axis', color='white')

xaxis = ts.options.scales.x_axes()
xaxis.ticks.fontColor = 'white'
xaxis.display = False
ts.options.legend.labels.fontColor = 'white'


# xaxis = ts.options.scales.add_x_axis()
# xaxis.gridLines.display = False

a = rptObj.ui.charts.chartJs.line(data, y_columns=[3, 4], x_axis='x')
donut = rptObj.ui.charts.chartJs.donut(data[:5], y_columns=[2], x_axis='x')
p = rptObj.ui.charts.chartJs.pie(data[:5], y_columns=[2], x_axis='x')
p.dataset().hoverBorderWidth = 10
p.click([
  p.js.reset()
])

rptObj.ui.button("Click").click([
  p.js.update(),

])

r = rptObj.ui.charts.chartJs.radar(data[:5], y_columns=[2, 3, 4], x_axis='x')
r.options.legend.labels.fontColor = 'white'
r.click([
  rptObj.js.alert("event", skip_data_convert=True)
])
polar = rptObj.ui.charts.chartJs.polar(data[:5], y_columns=[1], x_axis='x')
polar.options.add_title("Title", color="red")
#polar.click([
#  rptObj.js.console.log(polar.js.value)
#])
polar.options.legend.labels.fontColor = 'white'
for d in polar.datasets:
  d.borderWidth = 0

li = rptObj.ui.charts.chartJs.line(data, y_columns=list(range(4)), x_axis='x')
l = rptObj.ui.charts.chartJs.step(data, y_columns=list(range(4)), x_axis='x')
l.options.showLines = True
# l.options.scales.y_axis().ticks.max = 5
# l.options.scales.y_axis().ticks.min = 5
#l.options.scales.xAxes.ticks.min = 0

bu = rptObj.ui.charts.chartJs.bubble(data, y_columns=list(range(4)), x_axis='x', r_values=['r'])
bu.click([
  rptObj.js.console.log(bu.js.value)
])

s = rptObj.ui.charts.chartJs.scatter(data, y_columns=list(range(4)), x_axis='x')
s.click([
  rptObj.js.console.log(s.js.value)
])

h = rptObj.ui.charts.chartJs.hbar(data[:5], y_columns=list(range(4)), x_axis='x')
h.click([
  rptObj.js.console.log(h.js.value)
])

#b = rptObj.ui.charts.chartJs.bar(data, y_columns=[1, 2, 3], x_axis='x')
# b.add_dataset([2, 3, 4, 5, 6])

rptObj.ui.grid([
  [ts, r, li, polar],
#  [bu, b, h, a],
  [p, l, s, donut]
])

rptObj.ui.button("test").click([

])

rptObj.ui.tables.tabulators.table()


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)