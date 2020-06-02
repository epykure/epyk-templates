
import config
from epyk.core.Page import Report


# Create a basic report object
rptObj = Report(
  {'test': "this is a text",
   'test2': "this is a div"}
)
rptObj.headers.dev()

rptObj.ui.text(htmlCode="test")
rptObj.ui.div(htmlCode="test2")

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
