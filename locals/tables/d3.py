
from epyk.core.Page import Report
from epyk.tests import data_urls


# Create a basic report object
page = Report()
page.headers.dev()

data_rest_1 = page.py.requests.csv(data_urls.DC_QUAKES)

page.ui.tables.d3.table(data_rest_1)
