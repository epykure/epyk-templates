
from epyk.core.Page import Report

import config

rptObj = Report()

#
menu = rptObj.ui.context_menu(["Super", 'next'])
menu[0].click([
  rptObj.js.alert("Test")
])

rptObj.ui.layouts.new_line(10)
t = rptObj.ui.text("Test")
t.contextMenu(menu, [])

menu2 = rptObj.ui.context_menu([])
for d in [{'label': 'Python', 'url': 'https://www.python.org/'}, {'label': 'R'}]:
  menu2 += rptObj.ui.link(d['label'], d.get('url'))

rptObj.ui.layouts.new_line(5)
t2 = rptObj.ui.text("Test")
t2.contextMenu(menu2, [])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
