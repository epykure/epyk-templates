
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

rptObj.body.set_background()

data_rest_1 = rptObj.py.requests.csv(data_urls.DATA_EARTHQUAKE, store_location=r"C:\tmps")
data_rest_2 = rptObj.py.requests.csv(data_urls.AIRLINE_SAFETY, store_location=r"C:\tmps")

#rptObj.style.
t1 = rptObj.ui.tables.datatables.table(data_rest_1)
# t1.config.fixedHeader.activate()
# t1.config.fixedHeader.headerOffset = 100
# t1.config.colReorder = True
# t1.config.fixedColumns.leftColumns = 1
#t1.config.rowsGroup = [5]
t1.config.responsive.activate()
t1.config.select.activate()
#t1.config.scroller.activate()
# t1.config.buttons = ['copy', 'csv', 'excel', 'pdf']
#t1.config.rowGroup.activate()
# t1.config.scrollX = True
# t1.style.themes.nowrap()

t2 = rptObj.ui.tables.datatables.table(data_rest_2)
#t2.config.autoFill.activate()
t2.config.colReorder.activate()

#t.style.no_class()
#t.style.themes.bootstrap()
#t.get_column("airline")
#t.config.ajax = "./sources/arrays.txt"

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)