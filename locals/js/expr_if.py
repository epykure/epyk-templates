
import config

from epyk.core.Page import Report
from epyk.core.js import expr

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

input = rptObj.ui.input()

# Just generate a simple if statement on the value of the input
button = rptObj.ui.button("Click Me").click([
  expr
    .if_(input.dom.content.number >= 10, [rptObj.js.alert("Ok")])
    .elif_(input.dom.content == 'Other', [rptObj.js.alert("Other")])
    .else_([rptObj.js.alert("Else")
  ])
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
