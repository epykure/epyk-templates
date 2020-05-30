
from epyk.core.Page import Report
from epyk.tests import data_urls

from epyk.core.css.themes import ThemeBlue

import config


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

#rptObj.body.set_background()
#rptObj.theme = ThemeBlue.LightBlue()

#
#rptObj.imports().setVersion("tabulator", "3.4.3")

# rptObj.body.style.custom_class({'_attrs': {'text-align': 'center'}}, classname="tb-center")

data_rest_2 = rptObj.py.requests.csv(data_urls.AIRLINE_SAFETY, store_location=config.OUTPUT_TEMPS)
#data_rest_2[0]['airline'] = 'fab fa-python'
headers = list(data_rest_2[0].keys())
checks = rptObj.ui.lists.checks(headers, options={"checked": True})

js_data = rptObj.data.js.record(data=data_rest_2)
test = js_data.filterGroup("Test")

c = rptObj.ui.select(['airline'])
i = rptObj.ui.input("Aer Lingus")
f = rptObj.ui.panels.filters(options={"visible": True})

t1 = rptObj.ui.tables.tabulators.table(data_rest_2)
t2 = rptObj.ui.tables.tabulators.table(data_rest_2)

row = rptObj.ui.row([t1, t2])
row.options.noGutters = True
#
# i.enter([
#   f.dom.add(i.dom.content, c.dom.content),
#   rptObj.js.console.log(f.dom.content),
#   t1.build(test.match(f.dom.content))
# ])
#
#
# t1.config.paginationSize = 10
#
# c2 = t1.get_column("incidents_85_99")
# c2.formatters.wrapper("progress", {"height": '6px'}, {'color': ['red', 'orange', 'orange', 'green']})
#
# checks.click([
#     rptObj.js.console.log(checks.dom.unselected),
#     t1.js.hideColumna(checks.dom.unselected),
#     t1.js.showColumna(checks.dom.content),
#     t1.js.addRow({"airline": 'olivier', 'incidents_85_99': 400})
# ])
#
# d = rptObj.ui.drawer()
#
# select_all = rptObj.ui.button("Select")
# select_all.click([
#   checks.dom.selectAll(),
#   t1.js.hideColumna(checks.dom.unselected),
#   t1.js.showColumna(checks.dom.content)
# ])
#
# unselect_all = rptObj.ui.button("Unselect")
# unselect_all.click([
#   checks.dom.unSelectAll(),
#   t1.js.hideColumna(checks.dom.unselected),
#   t1.js.showColumna(checks.dom.content)
# ])
#
# d.add_panel([
#   rptObj.ui.titles.headline("Columns"),
#   select_all, unselect_all,
#   checks], [t1], display='block')

# c2.formatters.custom('''
#   function(cell, formatterParams){
#     var cell = cell.getTable().modules.format.getFormatter('progress').call(cell.getTable().modules.format, cell, formatterParams);
#     let frag = document.createRange().createContextualFragment(cell).firstChild;
#     frag.style.height = '4px';
#     console.log(cell);
#     return frag;
#   }
#   ''')

c = t1.get_column("avail_seat_km_per_week")#c.editor_input()
#c.formatter_number_format()
c.editors.input(search=False)
#c.editor_input_text({"A": {"color": 'red'}})
#c.mutator()

#c.formatter.extension("numbersFormat", module_alias="tabulator-numbers")
#c.formatterParams.data = {"precision": 3}
# c.formatterParams.css = {'color': 'blue'}
# c.formatterParams.pivot = "fatal_accidents_85_99"
# c.formatterParams.labels = ['lower bound', 'upper bound']


# t1.get_column("airline").formatter.extension("icon", module_alias="tabulator-icons")
# t1.get_column("airline").formatterParams.css = {"color": 'red', 'text-align': 'center'}
# t1.get_column("airline").formatterParams.tags = {"title": 'test'}

row = []
for rec in data_rest_2:
  row.append(rec['avail_seat_km_per_week'])
#t1.get_column("avail_seat_km_per_week").formatter.extension("numbers-intensity", module_alias="tabulator-numbers")

#t1.get_column("avail_seat_km_per_week").formatter.extension("password", module_alias="tabulator-inputs")
#t1.get_column("avail_seat_km_per_week").formatterParams.data = {"colors": ["white", "red"], 'steps': 20,  'intensity': 'incidents_85_99',  'css': {"text-align": 'center'}}

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
