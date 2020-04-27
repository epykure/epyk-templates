
from epyk.core.Page import Report

import config

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo


button = rptObj.ui.button("Test")

d = rptObj.ui.drawer()
d.add_panel(rptObj.ui.button("Test1"), "ok1")
d.add_panel(rptObj.ui.button("Test2"), "ok2")
d.add_panel(rptObj.ui.button("Test3"), "ok3")
d.set_handle(button)


d.drawers[0].click([
  d.dom.hide(),
  d.panels[0].dom.css({"display": 'block'}).r,
  rptObj.js.console.log(d.dom.content)
])

d.drawers[1].click([
  d.dom.hide(),
  d.panels[1].dom.css({"display": 'block'}),
  d.dom.delete(1)
])

d.drawers[2].click([
  d.dom.hide(),
  d.panels[2].dom.css({"display": 'block'}).r])


d1 = rptObj.ui.drawer()
d1.add_panel(rptObj.ui.button("Test"), "ok")
d1.drawers[0].click([d1.panels[0].dom.css({"display": 'block'})])

rptObj.ui.row([d, d1])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
