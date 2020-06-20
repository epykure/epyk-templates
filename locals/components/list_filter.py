
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

record = [
  {"text": 'text', 'icon': 'fas fa-times', 'checked': True, 'value': 8},
  {"text": 'abc', 'icon': 'fas fa-times', 'checked': True, 'value': 5},
  {"text": 'def', 'icon': 'fas fa-times', 'checked': True, 'value': 5},
  {"text": 'ghi', 'icon': 'fas fa-times', 'checked': True, 'value': 5},
]

data = page.data.js.record(data=record)
search = page.ui.inputs.search()

list = page.ui.lists.items(record, options={"badge": {"background": 'green'}, 'delete': True})

filter = data.filterGroup("test_filter")
search.enter([
  list.build(filter.any(search.dom.content))
])

