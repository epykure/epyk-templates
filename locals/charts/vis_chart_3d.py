
import config

from epyk.core.Page import Report
from epyk.tests import data_urls


rptObj = Report()
rptObj.headers.dev()

data = rptObj.py.requests.csv(data_urls.PLOTLY_POINTS, store_location=config.OUTPUT_TEMPS)

c = rptObj.ui._3d.vis.scatter(data, y_columns=["y"], x_axis="x", z_axis="z")

rptObj.ui.button("reset").click([
  c.build(  rptObj.data.vis.xyz(data[:6], y_columns=["x"], x_axis="x", z_axis="y") ),

])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
