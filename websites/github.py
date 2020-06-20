
from epyk.core.Page import Report#

page = Report()
page.body.style.css.padding = "0 70px"

page.ui.navbar(title="Epyk")

page.ui.text("epykure / epyk-ui")
tab = page.ui.panels.tabs()

for i in range(5):
  tab.add_panel("Panel %s" % i, page.ui.text("test %s" % i))

