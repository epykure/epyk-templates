from epyk.core.Page import Report#

import config

rptObj = Report()
rptObj.body.style.css.padding = "0 70px"

rptObj.ui.navbar(title="Epyk")

rptObj.ui.text("epykure / epyk-ui")
tab = rptObj.ui.panels.tabs()

for i in range(5):
  tab.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i))

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="web_github"))
