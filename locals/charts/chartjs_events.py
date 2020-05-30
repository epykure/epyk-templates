
import config

from epyk.core.Page import Report

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

js_data = rptObj.data.js.record(data=languages)
filter1 = js_data.filterGroup("filter1")

select = rptObj.ui.select([
  {"value": '', 'name': 'name'},
  {"value": 'type', 'name': 'code'},
])

c = rptObj.ui.charts.chartJs.bar(languages, y_columns=["rating", 'change'], x_axis='name')

checks = rptObj.ui.lists.checks(languages, column="name", options={"checked": True})

select.change([
  c.build(filter1.includes('name', checks.dom.content).group().sumBy(['rating', 'change'], select.dom.content, 'name'))
])

checks.click([
  rptObj.js.console.log(rptObj.js.objects.value),
  c.build(filter1.includes('name', checks.dom.content).group().sumBy(['rating', 'change'], select.dom.content, 'name'))
])

d = rptObj.ui.drawer()

select_all = rptObj.ui.button("Select")
select_all.click([
  checks.dom.selectAll(),
  c.build(filter1.includes('name', checks.dom.content).group().sumBy(['rating', 'change'], select.dom.content, 'name'))
])

unselect_all = rptObj.ui.button("UnSelect")
unselect_all.click([
  checks.dom.unSelectAll(),
  c.build(filter1.includes('name', checks.dom.content, empty_all=False).group().sumBy(['rating', 'change'], select.dom.content, 'name'))
])

d.add_panel([
  rptObj.ui.titles.headline("Columns"),
  select_all, unselect_all,
  checks], [c], display='block')

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
