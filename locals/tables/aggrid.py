
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

data_rest_1 = rptObj.py.requests.csv(data_urls.DC_QUAKES, store_location=config.OUTPUT_TEMPS)

table = rptObj.ui.tables.aggrid.table(data_rest_1)
table.config.sideBar.toolPanelsColumn()
# table.config.deltaColumnMode = True

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)