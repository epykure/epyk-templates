
import config

from epyk.core.Page import Report

rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

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


rptObj.ui.hidden("Test")

input = rptObj.ui.input()
chips = rptObj.ui.select(languages, column="type")

#
filters = rptObj.ui.panels.filters()

filter = rptObj.data.js.record(data=languages).filterGroup("test")
filter2 = rptObj.data.js.record(data=languages).filterGroup("test2")

c = rptObj.ui.charts.chartJs.bubble(languages, y_columns=["rating", 'change'], x_axis='name')
c.label(0, "Test")

data = [{"label": "python", "value": False}, {"label": "Java", "value": 5}]
checks1 = rptObj.ui.lists.checks(data)

checks2 = rptObj.ui.lists.checks(languages, column="name", options={"checked": True})

checks2.click([
  rptObj.js.console.log(rptObj.js.objects.value),
  c.build(filter.includes('name', checks2.dom.content)),
  #rptObj.js.console.log(rptObj.js.objects.value),
  #c.build(filter.equal('name', rptObj.js.objects.value)),
])

rptObj.ui.button("Test").click([
  rptObj.js.console.log(checks1.dom.content),
  rptObj.js.console.log(checks2.dom.content),
])

d = rptObj.ui.drawer()

select_all = rptObj.ui.button("Select")
select_all.click([
  checks2.dom.selectAll(),
  c.build(filter.includes('name', checks2.dom.content)),
])

unselect_all = rptObj.ui.button("UnSelect")
unselect_all.click([
  checks2.dom.unSelectAll(),
  c.build(filter.includes('name', checks2.dom.content, empty_all=False)),
])

d.add_panel([
  rptObj.ui.titles.headline("Columns"),
  select_all, unselect_all,
  checks2], [c], display='block')

#chips.delete([
  #rptObj.js.console.log(chips.dom.values()),
#  c.build(filter.includes('label', chips.dom.values())),
#])

chips.change([
  #rptObj.js.console.log(chips.dom.values()),
  c.build(filter.equal('name', input.dom.content)),
  c.build(filter.equal('type', chips.dom.content)),
])

# filters
input.enter([
  filters.dom.add(input.dom.content, 'name'),
  c.build(filter2.match(filters.dom.content, case_sensitive=False)),

])

rptObj.ui.button("reset").click([
  c.build(filter.equal('label', input.dom.content)),
  #c.js.render(),
])

rptObj.ui.button("add").click([
  #c.js.add('point', {'Test': 28}),
  #c.js.update(),
  c.js.remove(0, ["Test"]),
  c.js.load("Test2", [{'x': 0, 'y': 23}, {'x': 1, 'y': 23}]),
  c.js.unload(),
  c.js.update()
  #c.js.render(),
])

c.click([
  rptObj.js.console.log(c.js.content)
])

dataPoints3 = [
  {'label': "mango", 'x': 0, 'y': 20, 'y1': 20, 'r': 10},
  {'label': "grape", 'x': 1, 'y': 18, 'y2': 20, 'r': 5}
]

rptObj.ui.button("reset").click([
  c.build(dataPoints3),
  #c.build(dataPoints3, options={'z_columns': ['r']}),
  #c.js.render(),
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
