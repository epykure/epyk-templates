
from epyk.core.Page import Report

import config

rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

# Create two default rimepicker with different dates
first = rptObj.ui.fields.now(label="timestamp", color="red", helper="This is the report timestamp")
current = rptObj.ui.fields.now(label="Time field", deltatime=-60)

# Create a bespoke one with a fixed time
morning = rptObj.ui.fields.time("8:13:00", label="Time field")
morning.options.interval = 60

# Add event when the timepciker object change
morning.change([
  c.dom.write("time", skip_data_convert=True)
])

# Add button to retrieve the value of the different timepcickers
rptObj.ui.button("Click").click([
  c.dom.write(current.input.dom.content),
  c.dom.write(first.input.dom.val, stringify=True),
  first.input.js.value("9:00:00"),
  current.input.build("9:00:00"),
])

c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
