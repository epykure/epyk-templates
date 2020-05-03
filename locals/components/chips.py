from epyk.core.Page import Report

import config

rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
ch = rptObj.ui.chips(["example"])
ch.append("new data")
ch.enter([

])

rptObj.ui.button('Click').click([
  ch.dom.add(ch.dom.input),
  c.dom.write(ch.dom.content)
])

#
rptObj.ui.button('Add Fixed').click([
  ch.dom.add(ch.dom.input, fixed=True),
  c.dom.write(ch.dom.content)
])

#
icons = rptObj.ui.icons.bar(['fas fa-times', 'fas fa-anchor'])
icons[0].click([
  rptObj.js.alert("pl")
])
c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)

