
from epyk.core.Page import Report

import config

rptObj = Report()
rptObj.headers.dev()

#
menu = rptObj.ui.contextual(["Super", 'next'])
menu.add_item('test', 'fas fa-times')
menu[0].click([
  rptObj.js.alert("Test")
])

rptObj.ui.layouts.new_line(10)
t = rptObj.ui.text("Test")
t.contextMenu(menu, [])

menu2 = rptObj.ui.contextual([])
for d in [{'label': 'Python', 'url': 'https://www.python.org/'}, {'label': 'R'}]:
  menu2 += rptObj.ui.link(d['label'], d.get('url'))

rptObj.ui.layouts.new_line(5)
t2 = rptObj.ui.text("Test")
t2.contextMenu(menu2, [])

i = rptObj.ui.fields.input("test", label="test", options={"select": True})
i2 = rptObj.ui.fields.integer(options={"quantity": True, "select": True})
rptObj.ui.fields.static(label="readonly field")

b = rptObj.ui.button("Click")
rptObj.ui.navigation.side([i, i2, b], position="left")
# size = 200
# d = rptObj.ui.div("XXXXXXXXXXXXXXX")
# d.css({"position": 'absolute', 'top': 0, 'right': 0, 'height': '100%', 'overflow-x': 'hidden', 'margin-right': "-%spx" % size,
#        'width': "%spx" % size, 'border-left': '1px solid %s' % rptObj.theme.colors[5], 'padding': '5px'})
# rptObj.body.style.css.overflow_x = 'hidden'
#
# rptObj.ui.button("Click").click([
#   d.dom.toggle_transition("margin-right", "0px", "-%spx" % size),
# ])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
