
import config

from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()

div = rptObj.ui.div("&nbsp;")
div.style.attr_content("data-test")
div.attr["data-content"] = 'blue'
div.onReady([
  div.dom.attr("data-test", '1px solid red')
])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)