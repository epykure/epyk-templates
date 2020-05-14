from epyk.core.Page import Report

import config

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})


array = [1, 2, 3, 4, 5, 6]

rptObj.body.onReady([
  # This does not require a Javascript Name as the object will be just converted and used as is
  c.dom.write(rptObj.js.objects.list([1, 2, 3, 4, 5, 6]), stringify=True),

  # Create a non attached List and attached it to the report object before using the without feature
  c.dom.write(rptObj.js.objects.list(array, report=rptObj).without([3, 4]), stringify=True),

  # Transform a report object list and use underscore features
  # This will require a variable name as it will be stored on the javascript side
  c.dom.write(rptObj.data.js.list("test", array).sample(3).first(1), stringify=True),

# Transform a report object list and use underscore features
  # This will require a variable name as it will be stored on the javascript side
  c.dom.write(rptObj.data.js.list("test3", array).some.includes([3, 4]), stringify=True),

  # Transform a report object list and use underscore features
  # This will require a variable name as it will be stored on the javascript side
  c.dom.write(rptObj.data.js.list("test2", [1, 2, 3, 4, 5, 6]).sample(3).rest(1), stringify=True),
])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
