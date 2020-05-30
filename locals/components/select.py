
from epyk.core.Page import Report
from epyk.tests import data_urls

import config


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
data = rptObj.py.requests.csv(data_urls.AIRPORT_TRAFFIC, store_location=config.OUTPUT_TEMPS)

select = rptObj.ui.select(data, column="airport")
select.options.showTick = True
select.options.title = "Select title"

multi = rptObj.ui.select(data, column="city", multiple=True)
multi.options.actionsBox = False
multi.options.header = "Test Select"
multi.options.selectOnTab = True
multi.options.showTick = True

# Create a lookup object
lookupData = {"Akron-Canton Regional": [
  {"value": "A", 'text': "Example 1"},
  {"value": "B", 'text': "Example 2"}
]}
select2 = rptObj.ui.lookup(lookupData)

# Even on a select change
select.change([
  c.dom.write(select.dom.content),
  select2.build(select.dom.content)
], emtpyFncs=[
  c.dom.write("emtpy"),
])

# Even on a select change
select2.change([
  # Deselect all the items
  multi.js.deselectAll(),

  # Show the different items available to identify the selected items
  c.dom.write("===="),
  c.dom.write(select2.dom.text),
  c.dom.write(select2.dom.val, stringify=True),
  c.dom.write(select2.dom.content),
  c.dom.write(select2.dom.index),
])

# Show the selected value of the component
# The selected value will be the value and not the text visible
rptObj.ui.button("Get Multi Select").click([
  c.dom.write(multi.dom.content),
])

# Set the selection to two items
rptObj.ui.button("Set Chicago and Asheville").click([
  multi.js.val(['Chicago', 'Asheville'])
])

# Button event to transform selects
rptObj.ui.button("Remove Chicago").click([
  # Change the style of an item in the select
  multi.js.item("Chicago").css({"color": 'orange'}),
  multi.js.refresh(),

  # Remove a component from the select
  select.js.remove("Arcata"),
  c.dom.write("Chicago removed"),
])

c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)