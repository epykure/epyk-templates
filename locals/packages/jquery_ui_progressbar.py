
from epyk.core.Page import Report

import config

rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

# Create a progressbar (max 100)
b1 = rptObj.ui.sliders.progressbar(300, total=300)
b1.options.background = "red"

b2 = rptObj.ui.sliders.progressbar(50)

# Add event on the progress bar to change and retrieve the value
rptObj.ui.button("click").click([
  c.dom.write(b2.dom.content),
  b1.build(20),
  c.dom.write(b1.dom.val, stringify=True),
])

c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
