
from epyk.core.Page import Report

#
from epyk.core.data import events
from epyk.core.data import loops
from epyk.core.data import primitives

import config

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

table = rptObj.ui.tables.tabulator(languages)

table.drop([
  events.event.dataTransfer.text.trim().split(r"\n").forEach([
    loops.value.toString().trim().split(r"\t").setVar("split"),
    primitives.list(["name", 'type', 'rating', 'change']).setVar("cols"),
    primitives.dict({}, "row"),
    primitives.list(name="cols").forEach([
      primitives.dict(name="row").addItem(loops.value, primitives.list(name="split")[loops.i])
    ]),
    table.js.addRow(primitives.dict(name="row"))
  ])
])

# Javascript equivalent
# table.on("drop", [
#   #rptObj.js.console.log('event.dataTransfer.getData("text").split("\\n")', skip_data_convert=True),
#   '''
#   var cols = ["name", 'type', 'rating', 'change'];
#   event.dataTransfer.getData("text").split("\\n").forEach(function(line){
#     var split = line.split("\\t") ;
#     var row = {};
#     cols.forEach(function(col, i){ row[col] = split[i] });
#     %s.addRow(row);
#   })
#   ''' % table.js.varId
#   #table.js.addRow(
#
#   #  {"name": 'SQL', 'type': 'script', 'rating': 2.09, 'change': -0.47}
#   #)
# ])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
