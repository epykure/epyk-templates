
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

rptObj.body.set_background()
rptObj.imports().google_products(['tables'])

data_rest_1 = rptObj.py.requests.csv(data_urls.DATA_EARTHQUAKE, store_location=config.OUTPUT_TEMPS)

t1 = rptObj.ui.tables.google.table(data_rest_1)


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)