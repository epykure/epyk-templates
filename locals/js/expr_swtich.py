
import config

from epyk.core.Page import Report

from epyk.core.js import expr
from epyk.core.js import std

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

slider = rptObj.ui.slider()


slider.change([
  expr.switch(slider)
    .caseAbove(25, [std.alert("Above 25")])
    .caseRange(10, 24, [std.alert(slider.dom.content)])
    .caseBelow(10, [std.alert("Below 10")], include_value=False)
])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
