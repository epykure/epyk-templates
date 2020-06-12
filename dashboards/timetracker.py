
import config

from epyk.core.Page import Report

from epyk.core.data import events
from epyk.core.data import datamap


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()


side = rptObj.ui.navigation.side()

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

rptObj.ui.titles.head("Time")

col = rptObj.ui.col([
  rptObj.ui.fields.input(label="Comment", htmlCode="content"),
  rptObj.ui.fields.select(['background', 'range', 'box', 'point'], label="Categort", htmlCode="type"),
  rptObj.ui.date(label="Start Date", htmlCode="start"),
  rptObj.ui.date(label="End Date", htmlCode="end"),
  rptObj.ui.button("test", htmlCode="button")
])

dt = rptObj.ui.date(width=(220, 'px'), options={"inline": True})

rptObj.ui.row([dt, col])

timeline2 = rptObj.ui.charts.vis.timeline(data, content="content", start='start', end="end", type="type", group="group", options={"type": 'box'})
timeline2.options.stack = True
timeline2.setGroups(groups)

rptObj.components['button'].click([
  timeline2.js.addItem(datamap(rptObj.get_components(['content', 'type', 'start', 'end'])).attrs({"group": 3})),
  timeline2.js.fit()
])


scatter = rptObj.ui.charts.chartJs.bar([])
pie = rptObj.ui.charts.chartJs.pie([])

rptObj.ui.row([scatter, pie])

dt.select([
  rptObj.js.post("http://127.0.0.1:8000/data", jsData={"test": 4557}).onSuccess([
    scatter.build(events.data['chart']),
    pie.build(events.data['pie']),
    rptObj.js.console.log("data", skip_data_convert=True)
  ]),
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
