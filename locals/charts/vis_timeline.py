
from epyk.core.Page import Report
from epyk.core.data import datamap

from epyk.tests import data_urls


page = Report()
page.headers.dev()

data_earth = page.py.requests.csv(data_urls.DATA_EARTHQUAKE)
timeline = page.ui.charts.vis.timeline(data_earth[:30], content="place", start='time')

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

timeline2 = page.ui.charts.vis.timeline(data, content="content", start='start', end="end", type="type", group="group", options={"type": 'box'})
timeline2.options.stack = True
timeline2.setGroups(groups)

content = page.ui.fields.input(label="Comment")
category = page.ui.fields.select(['background', 'range', 'box', 'point'], label="Categort")
start = page.ui.date(label="Start Date")
end = page.ui.date(label="End Date")

page.ui.toggle({"off": 'Me', 'on': "Team"})

page.ui.button("test").click([
  timeline2.js.addItem(datamap().add(start.input, 'start').add(end.input, 'end').add(category, 'type').add(content, 'content').attrs({"group": 3})),
  timeline.js.fit()
])
