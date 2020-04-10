
import config

from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()


# Trigger a function when a key is pressed on the page
rptObj.ui.text("Press enter to display hello World")
rptObj.js.addKeyEvent([rptObj.js.alert('Hello World')], 13)

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_js_event"))
