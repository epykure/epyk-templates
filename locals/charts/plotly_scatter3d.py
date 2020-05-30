
import config

from epyk.core.Page import Report
from epyk.tests import data_urls


rptObj = Report()
rptObj.headers.dev()

data = rptObj.py.requests.csv(data_urls.PLOTLY_WEBGL_POLAR, store_location=config.OUTPUT_TEMPS)


s3d = rptObj.ui.charts.plotly.scatter3d(data, y_columns=["trial_1_theta", "trial_2_theta"], x_axis="trial_3_r", z_axis=["trial_1_r", "trial_2_r"])
s3d.data.opacity = 0.5
s3d.layout.grid_colors('white')
s3d.layout.axis_colors('white')
s3d.layout.no_background()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
