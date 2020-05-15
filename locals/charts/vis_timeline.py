
import config

from epyk.core.Page import Report
from epyk.tests import data_urls


rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

data_earth = rptObj.py.requests.csv(data_urls.DATA_EARTHQUAKE, store_location=config.OUTPUT_TEMPS)
timeline = rptObj.ui.charts.vis.timeline(data_earth[:30], y_columns=["place"], x_axis='time')


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
