
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

data_rest_1 = rptObj.py.requests.json(data_urls.PIVOTTABLE_DATA, store_location=r"C:\tmps")

tb2 = rptObj.ui.tables.pivots.plotly(data_rest_1, [], [])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)