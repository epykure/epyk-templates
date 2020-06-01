# https://developers.google.com/maps/documentation

from epyk.core.Page import Report

from epyk.core.js import General
from epyk.core.data import loops

# Using data and JavaScript shortcuts


import config

# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

menu1 = rptObj.ui.div("menu", htmlCode="test_menu_1")
menu1.attr["name"] = "menu"
menu1.style.css.height = 0
menu1.style.css.top = 0
menu1.style.css.position = 'fixed'

menu2 = rptObj.ui.div("menu2", htmlCode="test_menu_2")
menu2.attr["name"] = "menu"
menu2.style.css.height = 0
menu2.style.css.top = 0
menu2.style.css.position = 'fixed'

divA = rptObj.ui.div("Test 1")
divB = rptObj.ui.div("Test 2")

div = rptObj.ui.div([
  divA,
  divB,
])
div.style.css.top = 0
div.style.css.position = 'fixed'
div.style.css.background = 'green'
div.style.css.height = '50px'
div.style.css.color = 'white'

divA.click([
  General.dom.querySelectorAll("[name=menu]:not([id=test_menu_1])").forEach([
    loops.dom.css({"height": 0, "margin-top": 0})]),

  menu1.dom.toggleAttrs("height", "200px", {"height": "200px", "margin-top": "50px"},
                       {"height": 0, "margin-top": 0}),
])


divB.click([
  General.dom.querySelectorAll("[name=menu]:not([id=test_menu_2])").forEach([
    loops.dom.css({"height": 0, "margin-top": 0})]),

  menu2.dom.toggleAttrs("height", "200px", {"height": "200px", "margin-top": "50px"},
                       {"height": 0, "margin-top": 0}),

])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
