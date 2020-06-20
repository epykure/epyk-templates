
import config

from epyk.core.Page import Report

# Create a basic report object
page = Report()

page.ui.text("#This is a text", options={"markdown": True})
page.ui.button("This is a test").click([
  page.js.alert("test")
])

page.outs.publish(server="node", app_path=config.OUTPUT_PATHS_LOCALS_TS, module=config.OUT_FILENAME)