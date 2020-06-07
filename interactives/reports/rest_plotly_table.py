
import os

import config
from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

languages = [
  {"name": 'C', 'type': 'code', 'rating': 17.07, 'change': 12.82},
  {"name": 'Java', 'type': 'code', 'rating': 16.28, 'change': 0.28},
  {"name": 'Python', 'type': 'script', 'rating': 9.12, 'change': 1.29},
  {"name": 'C++', 'type': 'code', 'rating': 6.13, 'change': -1.97},
  {"name": 'C#', 'type': 'code', 'rating': 4.29, 'change': 0.3},
  {"name": 'Visual Basic', 'type': 'script', 'rating': 4.18, 'change': -1.01},
  {"name": 'JavaScript', 'type': 'script', 'rating': 2.68, 'change': -0.01},
  {"name": 'PHP', 'type': 'script', 'rating': 2.49, 'change': 0},
  {"name": 'SQL', 'type': 'script', 'rating': 2.09, 'change': -0.47},
  {"name": 'R', 'type': 'script', 'rating': 1.85, 'change': 0.90},
]

table = rptObj.ui.tables.plotly(languages)

rptObj.ui.button("Click").click([
  rptObj.js.post("/data_table_plotly").onSuccess([
    table.build(rptObj.js.objects.data['content']),
    #table.js.hideColumns(rptObj.js.objects.data['columns']),
    #table.js.showColumns(rptObj.js.objects.data['visible']),
    #table.js.addRow(rptObj.js.objects.data['row']),
  ])
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_INTERACTIVE, name=os.path.basename(__file__)[:-3])
