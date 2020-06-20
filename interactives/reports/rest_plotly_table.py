
from epyk.core.Page import Report

from epyk.tests import mocks


# Create a basic report object
page = Report()
page.headers.dev()


table = page.ui.tables.plotly(mocks.languages)

page.ui.button("Click").click([
  page.js.post("/data_table_plotly").onSuccess([
    table.build(page.js.objects.data['content']),
    #table.js.hideColumns(page.js.objects.data['columns']),
    #table.js.showColumns(page.js.objects.data['visible']),
    #table.js.addRow(page.js.objects.data['row']),
  ])
])

