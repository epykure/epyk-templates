
import config

from epyk.core.Page import Report
from epyk.core.css.themes import ThemeDark

# Create a basic report object
rptObj = Report()

#
tabs = rptObj.ui.panels.tabs()
tabs.options.css_tab_clicked = {"border-bottom": '1px solid red', "background": 'white'}

for i in range(5):
  if i % 2:
    tabs.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i), css_tab_clicked={"background": 'yellow'})
  else:
    tabs.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i), selected=True)
tabs.select("Panel 2")

rptObj.ui.button("Click").click([
  tabs.dom.add_tab("New tab"),
  rptObj.js.console.log(tabs.dom.selected_index),
  tabs.dom.deselect_tabs(),
  tabs.panel("Panel 2").dom.transition("color", 'red', duration=1, reverse=True)
])

up = rptObj.ui.panels.arrows_up()
for i in range(5):
  up.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i), selected=True)

down = rptObj.ui.panels.arrows_down()
for i in range(5):
  down.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i), selected=True)

menu = rptObj.ui.panels.menu()
for i in range(5):
  menu.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i), selected=True)

pills = rptObj.ui.panels.pills()
for i in range(5):
  pills.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i), selected=True)

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)