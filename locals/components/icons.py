
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()

menu = rptObj.ui.layouts.icons()
menu.add_icon("fab fa-accusoft")
menu.add_icon("fab fa-accusoft")

menu.icon.click([menu.icon.dom.css({"color": 'red'})])

rptObj.ui.icons.signin("RRR")

env = rptObj.ui.icons.awesome(rptObj.ui.icons.get.ICON_ENVELOPE, text=2)
#env.icon_css({"background": 'MistyRose', 'font-size': '20px'})
#env.span.style.addCls("fa-layers-counter")

edit = rptObj.ui.icons.edit()
edit.on('click', rptObj.js.console.log('test'))

rptObj.ui.icons.clock().css({"color": 'blue'})
#rptObj.ui.icons.edit().color("red")



rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
