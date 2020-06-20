
from epyk.core.Page import Report

from epyk.tests import data_urls


# Create a basic report object
page = Report()
page.headers.dev()

data_rest_1 = page.py.requests.csv(data_urls.DC_QUAKES)

table1 = page.ui.tables.aggrids.table(data_rest_1)
table2 = page.ui.tables.aggrids.table(data_rest_1)

page.ui.row([
  page.ui.col([
    page.ui.titles.title("Test"),
    table1]), table2])
#table.config.sideBar.toolPanelsColumn()
# table.config.deltaColumnMode = True
