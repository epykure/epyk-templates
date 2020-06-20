
from epyk.core.Page import Report

from epyk.tests import data_urls


page = Report()
page.headers.dev()

data = page.py.requests.csv(data_urls.PLOTLY_POINTS)

c = page.ui._2d.vis.bar(data, y_columns=["y"], x_axis="x")

page.ui.button("reset").click([
  c.build(  page.data.vis.xy(data[:6], y_columns=["x"], x_axis="x") ),
  page.js.console.log(c.js.getDataRange())
])

