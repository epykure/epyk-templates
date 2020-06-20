
from epyk.core.Page import Report

from epyk.tests import data_urls


# Create a basic report object
page = Report()
page.headers.dev()

data_rest_1 = page.py.requests.json(data_urls.PIVOTTABLE_DATA)

tb2 = page.ui.tables.pivots.plotly(data_rest_1, [], [])

