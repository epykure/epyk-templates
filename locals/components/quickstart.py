
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

bar = page.ui.charts.chartJs.bar(mocks.languages, y_columns=["rating", 'change'], x_axis='name')
pie = page.ui.charts.chartJs.pie(mocks.languages, y_columns=['change'], x_axis='name')
page.ui.row([bar, pie])

select.change([
  bar.build(filter1.group().sumBy(['rating', 'change'], select.dom.content, 'name')),
  pie.build(filter1.group().sumBy(['change'], select.dom.content, 'name')),
])