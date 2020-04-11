
import config

from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()

# Add the file from the local environment context defined in Imports.STATIC_PATH
# This path will be overridden and specific to your configuration
rptObj.js.customFile("test.js")


print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_js_custom"))
