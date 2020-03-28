
from epyk.core.Page import Report
from epyk.tests import data_urls

import config


# Create a basic report object
rptObj = Report()
rptObj.body.set_background()

# Input data
data = config.getSeries(5, 40)
data_rest = rptObj.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES, store_location=config.OUTPUT_TEMPS)

scatter = rptObj.ui.charts.nvd3.scatter(data, y_columns=[1, 2, 3, 4], x_axis='x', title="Scatter chart")
scatter.dom.showYAxis(False).showXAxis(False)

records = [
    {'name': 'scripts',
     'children': [
        {"name": "javascript", "size": 10},
        {"name": "python", "size": 5},
        {"name": "ruby", "size": 5},
        {"name": "r", "size": 5}]},
     {"name": "code",
      "children": [
        {"name": "C#", "size": 10},
        {"name": "Java", "size": 5},
      ]
      }
  ]

force = rptObj.ui.charts.nvd3.forceDirected()
force.add_trace({
    "nodes": [
      {"name": "Myriel", "group":1},
      {"name": "Napoleon", "group":1},
      {"name": "Mlle.Baptistine", "group": 5}],
    "links": [
      {"source": 1, "target": 2, "value": 1}
    ]
})

sunburst = rptObj.ui.charts.nvd3.sunburst(records, name='languages')
sc = rptObj.ui.charts.nvd3.candlestick(data_rest, closes=["AAPL.Close"], highs=["AAPL.High"], lows=["AAPL.Low"], opens=["AAPL.Open"], x_axis='Date')
ohlc = rptObj.ui.charts.nvd3.ohlc(data_rest, closes=["AAPL.Close"], highs=["AAPL.High"], lows=["AAPL.Low"], opens=["AAPL.Open"], x_axis='Date')

plot_box = rptObj.ui.charts.nvd3.group_box()
plot_box.add_box(q1=1.05, q3=2.7, mean=3.365, median=1.3, minRegularValue=0.4, maxRegularValue=4.4, minOutlier=0.4, maxOutlier=6)
plot_box.add_box(q1=1.05, q3=2.849999996, mean=3.4949999, median=1.5, minRegularValue=0.3, maxRegularValue=4.9, minOutlier=0.3, maxOutlier=4.9)


multi = rptObj.ui.charts.nvd3.multi(data, y_columns=[1, 2], x_axis='x', title="multi")
histo = rptObj.ui.charts.nvd3.histo(data, y_columns=[1, 2], x_axis='x', title='histo')
area = rptObj.ui.charts.nvd3.area(data, y_columns=[3, 4], x_axis='x', title='Area')

bar = rptObj.ui.charts.nvd3.bar(data, y_columns=[1], x_axis='x', title="Discrete bar")
multibar = rptObj.ui.charts.nvd3.bar(data, y_columns=[1, 2, 3, 4], x_axis='x', title="Multi bar")
hbar = rptObj.ui.charts.nvd3.hbar(data, y_columns=[1, 2, 3, 4], x_axis='g', title="Horizontal bar")

line = rptObj.ui.charts.nvd3.line(data, y_columns=[1, 2, 3, 4], x_axis='x')
cumul = rptObj.ui.charts.nvd3.line_cumulative(data, y_columns=[1, 2, 3, 4], x_axis='x')
line_focus = rptObj.ui.charts.nvd3.line_focus(data, y_columns=[1, 2, 3, 4], x_axis='x')
parallel_coordinates = rptObj.ui.charts.nvd3.parallel_coordinates(data, dimensions=[1, 2, 3, 4])
parallel_coordinates.dom.lineTension(.2)

pie = rptObj.ui.charts.nvd3.pie(data, y_column=1, x_axis='g')
donut = rptObj.ui.charts.nvd3.donut(data, y_column=1, x_axis='g')
donut_s = rptObj.ui.charts.nvd3.donut(data, y_column=1, x_axis='g')
donut_s.dom.padAngle(.08).cornerRadius(5)

#
# rptObj.body.style.custom_class(css_attrs={"_attrs": {"fill": 'red'}}, classname='nvd3.nv-pie .nv-pie-title')
# #rptObj.body.style.add_custom_class(css_attrs={"_attrs": {"fill": 'red'}}, classname='nvd3.nv-pie .nv-pie-title')
#
# toto = rptObj.ui.text("toto")
# toto.style.add_custom_class("super", {"_attrs": {"color": 'red'}})

gauge = rptObj.ui.charts.nvd3.gauge(value=8, text="", total=10)

rptObj.ui.grid([
  [ohlc, force, plot_box],
  [sc, sunburst, parallel_coordinates],
  [bar, multibar, hbar],
  [scatter, gauge],
  [multi, histo, area],
  [line, cumul, line_focus],
  [pie, donut, donut_s]
])


print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_charts_nvd3"))
