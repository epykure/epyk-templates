
import config

from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()
rptObj.headers.dev()


input = rptObj.ui.input(options={'reset': True})
container = rptObj.ui.network.news() # options={"dated": False}
side = rptObj.ui.navigation.side([container])
side2 = rptObj.ui.navigation.side([])

button = rptObj.ui.button("Add news")
button.click([
  container.build(input.dom.content)
])


replay = rptObj.ui.button("Reset")
replay.click([
  container.js.reset(),

])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)