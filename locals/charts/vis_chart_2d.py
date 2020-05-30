
import config

from epyk.core.Page import Report
from epyk.tests import data_urls


rptObj = Report()
rptObj.headers.dev()

data = rptObj.py.requests.csv(data_urls.PLOTLY_POINTS, store_location=config.OUTPUT_TEMPS)

c = rptObj.ui._2d.vis.bar(data, y_columns=["y"], x_axis="x")

rptObj.ui.button("reset").click([
  c.build(  rptObj.data.vis.xy(data[:6], y_columns=["x"], x_axis="x") ),
  rptObj.js.console.log(c.js.getDataRange())
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
