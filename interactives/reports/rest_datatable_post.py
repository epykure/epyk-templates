
from epyk.core.Page import Report

from epyk.tests import mocks


# Create a basic report object
page = Report()
page.headers.dev()

table1 = page.ui.tables.datatable(mocks.languages)
table2 = page.ui.tables.datatable(mocks.languages)

page.ui.row([table1, table2])

page.ui.button("Click").click([
  page.js.post("/data_datatable").onSuccess([
    table1.build(page.js.objects.data['content']),
    #table.js.hideColumns(page.js.objects.data['columns']),
    #table.js.showColumns(page.js.objects.data['visible']),
    #table.js.addRow(page.js.objects.data['row']),
  ])
])
