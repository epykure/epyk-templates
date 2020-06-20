
from epyk.core.Page import Report

from epyk.core.data import events
from epyk.core.data import datamap


# Create a basic report object
page = Report()
page.headers.dev()


side = page.ui.navigation.side()

data = [
    {"id": 0, "group": 0, "content": 'item 0', "start": "2020-06-29", 'type': 'point'},
    {"id": 0, "group": 0, "content": 'item 0', "start": "2020-06-17", "end": "2020-06-21"},
    {"id": 1, "group": 0, "content": 'item 1', "start": "2020-06-10", "end": "2020-06-20", 'type': 'background'},
    {"id": 2, "group": 1, "content": 'item 2', "start": "2020-06-16", "end": "2020-06-24"},
    {"id": 3, "group": 1, "content": 'item 3', "start": "2020-06-23", "end": "2020-06-24", 'type': 'box'},
    {"id": 4, "group": 1, "content": 'item 4', "start": "2020-06-24", "end": "2020-06-26"},
    {"id": 5, "group": 2, "content": 'item 5', "start": "2020-06-24", "end": "2020-06-27"}
  ]

groups = [
  {"id": 1, 'content': 'test 1'},
  {"id": 2, 'content': 'test 2'},
  {"id": 3, 'content': 'test 3'},
  {"id": 0, 'content': 'test 0'},
]

page.ui.titles.head("Time")

col = page.ui.col([
  page.ui.fields.input(label="Comment", htmlCode="content"),
  page.ui.fields.select(['background', 'range', 'box', 'point'], label="Categort", htmlCode="type"),
  page.ui.date(label="Start Date", htmlCode="start"),
  page.ui.date(label="End Date", htmlCode="end"),
  page.ui.button("test", htmlCode="button")
])

dt = page.ui.date(width=(220, 'px'), options={"inline": True})

page.ui.row([dt, col])

timeline2 = page.ui.charts.vis.timeline(data, content="content", start='start', end="end", type="type", group="group", options={"type": 'box'})
timeline2.options.stack = True
timeline2.setGroups(groups)

page.components['button'].click([
  timeline2.js.addItem(datamap(page.get_components(['content', 'type', 'start', 'end'])).attrs({"group": 3})),
  timeline2.js.fit()
])


scatter = page.ui.charts.chartJs.bar([])
pie = page.ui.charts.chartJs.pie([])

page.ui.row([scatter, pie])

dt.select([
  page.js.post("http://127.0.0.1:8000/data", jsData={"test": 4557}).onSuccess([
    scatter.build(events.data['chart']),
    pie.build(events.data['pie']),
    page.js.console.log("data", skip_data_convert=True)
  ]),
])

