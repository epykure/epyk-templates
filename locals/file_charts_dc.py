
from epyk.core.Page import Report
from epyk.tests import data_urls

import config


rptObj = Report()
rptObj.body.set_background()

# Create a Javascript Crossfilter object
data = config.getSeries(5, 30)
crossfilter = rptObj.js.data.crossfilter(data, "test")
dimension = crossfilter.dimension([('x', int)], 'test_dim')
group = dimension.group('group').reduceSum(1)

# Write the object to the Javascript page
rptObj.body.onLoad([
  crossfilter, dimension, group
])

# Create a DC line chart and add crossfilter definition
line1 = rptObj.ui.charts.dc.line() # data, y_columns=[1, 2], x_axis='x'
line1.crossFilter(dimension, group)

# Create a DC line chart and add crossfilter definition
pie2 = rptObj.ui.charts.dc.pie(height=(150, "px")) # data, y_columns=[1, 2], x_axis='x'
pie2.crossFilter(dimension, group)

# Create a DC line chart and add crossfilter definition
pie3 = rptObj.ui.charts.dc.bar(height=(150, "px")) # data, y_columns=[1, 2], x_axis='x'
pie3.crossFilter(dimension, group)

#
data = config.getSeries(5, 30)
line = rptObj.ui.charts.dc.line(data, y_columns=[1, 2], x_axis='x')
step = rptObj.ui.charts.dc.step(data, y_columns=[1, 2], x_axis='x')
bar = rptObj.ui.charts.dc.bar(data, y_columns=[3, 4], x_axis='x')
hbar = rptObj.ui.charts.dc.hbar(data[:10], y_column=4, x_axis='x')
pie = rptObj.ui.charts.dc.pie(data[:5], y_column=3, x_axis='x')
scatter = rptObj.ui.charts.dc.scatter(data, y_columns=[2, 4], x_axis='x')
bubble = rptObj.ui.charts.dc.bubble(data, y_columns=3, x_axis='x', r_axis=4, options={'statc_factor': '/10'})

# Report layout
rptObj.ui.title("DC Charts")
rptObj.body.style.css.padding = "0 10px"

# Report grid
rptObj.ui.grid([
  [rptObj.ui.col([
      rptObj.ui.title("DC Line chart", level=4),
      rptObj.ui.text("Example of a "),
      line1
   ]),
   rptObj.ui.col([
     rptObj.ui.title("DC Line chart", level=4),
     rptObj.ui.row([
       rptObj.ui.text("Example of a "),
       pie2
     ]),
     rptObj.ui.row([
       pie3,
       rptObj.ui.text("Example of a ")
     ])
   ])
  ],
  [rptObj.ui.title("Bespoke Examples", level=4).css({"color": 'black'})],
  [line, step, scatter],
  [bar, hbar],
  [bubble, pie],
])


print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_charts_dc"))
