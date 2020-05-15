
import config

from epyk.core.Page import Report


rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

data_series = config.getSeries(5, 30)

sur = rptObj.ui.charts.plotly.surface(data_series, y_columns=[1], x_axis='x', z_axis=2)

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
