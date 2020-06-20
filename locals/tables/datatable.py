
from epyk.core.Page import Report

from epyk.tests import data_urls


# Create a basic report object
page = Report()
page.headers.dev()

page.body.set_background()

data_rest_1 = page.py.requests.csv(data_urls.DATA_EARTHQUAKE)
data_rest_2 = page.py.requests.csv(data_urls.AIRLINE_SAFETY)

#page.style.
t1 = page.ui.tables.datatables.table(data_rest_1)
t1_bis = page.ui.tables.datatable(data_rest_1)


page.ui.grid([[t1, t1_bis]])

# t1.config.fixedHeader.activate()
# t1.config.fixedHeader.headerOffset = 100
# t1.config.colReorder = True
# t1.config.fixedColumns.leftColumns = 1
#t1.config.rowsGroup = [5]
#t1.config.responsive.activate()
#t1.config.select.activate()

#t1.config.scroller.activate()
# t1.config.buttons = ['copy', 'csv', 'excel', 'pdf']
#t1.config.rowGroup.activate()
# t1.config.scrollX = True
# t1.style.themes.nowrap()

#t2 = page.ui.tables.datatables.table(data_rest_2)
#t2.config.autoFill.activate()
#t2.config.colReorder.activate()

#t.style.no_class()
#t.style.themes.bootstrap()
#t.get_column("airline")
#t.config.ajax = "./sources/arrays.txt"
