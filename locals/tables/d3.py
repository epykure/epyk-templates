
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

data_rest_1 = rptObj.py.requests.csv(data_urls.DC_QUAKES, store_location=config.OUTPUT_TEMPS)

rptObj.ui.tables.d3.table(data_rest_1)

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)