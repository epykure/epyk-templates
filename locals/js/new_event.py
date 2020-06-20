
from epyk.core.Page import Report
from epyk.core.js import std


# Create a basic report object
page = Report()
page.headers.dev()

div = page.ui.div("Test")
div.onReady([
  # Create a bespoke type of event
  div.dom.addEventListener("build", std.alert("Ok"))
])

div2 = page.ui.div("Trigger Event")
div2.click([
  # Iitiate the event
  std.createEvent('test_event'),
  std.initEvent("build", 'test_event', True, True),

  # Dispatch this event to trigger the component div
  div2.dom.dispatchEvent(std.getEvent('test_event'))
])

