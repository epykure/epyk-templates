
from epyk.core.Page import Report

from epyk.tests import mocks


page = Report()
page.headers.dev()


js_data = page.data.js.record(data=mocks.languages)
filter1 = js_data.filterGroup("filter1")

select = page.ui.select([
  {"value": '', 'name': 'name'},
  {"value": 'type', 'name': 'code'},
])

c = page.ui.charts.chartJs.bar(mocks.languages, y_columns=["rating", 'change'], x_axis='name')

checks = page.ui.lists.checks(mocks.languages, column="name", options={"checked": True})

select.change([
  c.build(filter1.includes('name', checks.dom.content).group().sumBy(['rating', 'change'], select.dom.content, 'name'))
])

checks.click([
  page.js.console.log(page.js.objects.value),
  c.build(filter1.includes('name', checks.dom.content).group().sumBy(['rating', 'change'], select.dom.content, 'name'))
])

d = page.ui.drawer()

select_all = page.ui.button("Select")
select_all.click([
  checks.dom.selectAll(),
  c.build(filter1.includes('name', checks.dom.content).group().sumBy(['rating', 'change'], select.dom.content, 'name'))
])

unselect_all = page.ui.button("UnSelect")
unselect_all.click([
  checks.dom.unSelectAll(),
  c.build(filter1.includes('name', checks.dom.content, empty_all=False).group().sumBy(['rating', 'change'], select.dom.content, 'name'))
])

d.add_panel([
  page.ui.titles.headline("Columns"),
  select_all, unselect_all,
  checks], [c], display='block')

