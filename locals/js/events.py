
import config

from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()

# Add a title to the report
rptObj.ui.title("Events on the page", level=3)

# Trigger a function when a key is pressed on the page
rptObj.ui.text("Press enter to display hello World")
rptObj.js.addKeyEvent([rptObj.js.alert('Hello World')], 13)

# Add a title to the report
rptObj.ui.title("Events on a component", level=3)

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)