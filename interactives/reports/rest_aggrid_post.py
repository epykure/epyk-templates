
from epyk.core.Page import Report

from epyk.tests import mocks


# Create a basic report object
page = Report()
page.headers.dev()

table = page.ui.tables.aggrid(mocks.languages)
table2 = page.ui.tables.aggrid(mocks.languages)

page.ui.row([table, table2])

page.ui.button("Click").click([
  page.js.post("/data_table").onSuccess([
    table.build(page.js.objects.data['content']),
    page.js.console.log(table.js.getSortModel() ),

    page.js.console.log(table.js.getDisplayedRowCount()),
    table.js.hideColumns(page.js.objects.data['columns']),
    table.js.showColumns(page.js.objects.data['visible']),
    page.js.console.log( table.js.columnApi.getColumn('name') ) ,
    #table.js.addRow(page.js.objects.data['row']),
  ])
])

