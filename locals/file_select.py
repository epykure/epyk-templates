
from epyk.core.Page import Report
from epyk.tests import data_urls

import config


# Create a basic report object
rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
data = rptObj.py.requests.csv(data_urls.AIRPORT_TRAFFIC, store_location=config.OUTPUT_TEMPS)

select = rptObj.ui.select(data, column="airport")
multi = rptObj.ui.select(data, column="city", multiple=True)

# Create a lookup object
lookupData = {"Akron-Canton Regional": [
  {"value": "A", 'text': "Example 1"},
  {"value": "B", 'text': "Example 2"}
]}
select2 = rptObj.ui.lookup(lookupData)

# Even on a select change
select.change([
  c.write(select.dom.content),
  select2.build(select.dom.content)
], emtpyFncs=[
  c.write("emtpy"),
])

# Even on a select change
select2.change([
  # Deselect all the items
  multi.js.deselectAll(),

  # Show the different items available to identify the selected items
  c.write("===="),
  c.write(select2.dom.text),
  c.write(select2.dom.val, stringify=True),
  c.write(select2.dom.content),
  c.write(select2.dom.index),
])

# Show the selected value of the component
# The selected value will be the value and not the text visible
rptObj.ui.button("Get Multi Select").click([
  c.write(multi.dom.content),
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
  c.write("Chicago removed"),
])

c.move()

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_select"))