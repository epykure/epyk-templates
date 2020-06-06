
import config

from epyk.core.Page import Report
from epyk.core.js import std


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Add a title to the report
rptObj.ui.title("Events on the page", level=3)

# Trigger a function when a key is pressed on the page
rptObj.ui.text("Press enter to display hello World")

# Add keyup event to the page itself
rptObj.js.keyup.enter(std.alert('Hello World'))

# Add a title to the report
rptObj.ui.title("Events on a component", level=3)

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)