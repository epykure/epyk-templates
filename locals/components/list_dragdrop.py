

from epyk.core.Page import Report
from epyk.core.data import datamap, events


# Create a basic report object
page = Report()
page.headers.dev()

list = page.ui.list(["A", "B", "C"])
for i in list:
  i.draggable()

div = page.ui.div("No dropped value", htmlCode='content')
div.style.css.padding = 5
div.drop([
  div.build(events.data)
])