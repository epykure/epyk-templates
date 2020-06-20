
from epyk.core.Page import Report

from epyk.tests import mocks

#
from epyk.core.data import events
from epyk.core.data import loops
from epyk.core.data import primitives


# Create a basic report object
page = Report()
page.headers.dev()

table = page.ui.tables.tabulator(mocks.languages)
for c in table.config._attrs.get('columns', []):
  c.exts.formatters.drag_and_drop()
  # c.formatters.custom('''
  #   function(cell, formatterParams){
  #     var cellElement = cell.getElement();
  #
  #     cellElement.ondragover = function(e) { event.preventDefault() };
  #
  #     cellElement.addEventListener('drop', (function(cell){
  #       return function(){
  #         var pos = -1;
  #         var rowIndex = cell.getRow().getPosition();
  #         var cells = cell.getRow().getCells();
  #         var row = cell.getRow();
  #         cells.forEach(function(c, i){
  #           if (c.getColumn().getField() == cell.getColumn().getField() ) {
  #               pos = i
  #           }
  #         });
  #
  #         console.log(event.dataTransfer.getData("text"));
  #         console.log(pos);
  #         console.log(rowIndex);
  #
  #         event.dataTransfer.getData("text").trim().split("\\n").forEach(function(line){
  #           line.trim().split("\\t").forEach(function(v, j){
  #             cells[pos + j].setValue(v)
  #           });
  #           row = row.getNextRow();
  #           cells = row.getCells();
  #
  #         })
  #       }
  #       })(cell)
  #     );
  #
  #     cell.getElement().onclick = function(e){ alert("") } ;
  #
  #     return cell.getValue(); } ''')
  # print(type(c))
# "function(data, type, row, meta) { console.log(row) }

# table.drop([
#   events.event.dataTransfer.text.trim().split(r"\n").forEach([
#     loops.value.toString().trim().split(r"\t").setVar("split"),
#     primitives.list(["name", 'type', 'rating', 'change']).setVar("cols"),
#     primitives.dict({}, "row"),
#     primitives.list(name="cols").forEach([
#       primitives.dict(name="row").addItem(loops.value, primitives.list(name="split")[loops.i])
#     ]),
#     table.js.addRow(primitives.dict(name="row"))
#   ])
# ])

# Javascript equivalent
# table.on("drop", [
#   #page.js.console.log('event.dataTransfer.getData("text").split("\\n")', skip_data_convert=True),
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

