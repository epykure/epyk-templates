
from epyk.core.Page import Report

from epyk.tests import data_urls


# Create a basic report object
page = Report()
page.headers.dev()

page.body.set_background()
page.imports().google_products(['tables'])

data_rest_1 = page.py.requests.csv(data_urls.DATA_EARTHQUAKE)

t1 = page.ui.tables.google.table(data_rest_1)

