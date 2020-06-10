# https://developers.google.com/maps/documentation

from epyk.core.Page import Report

from epyk.core.js import std
from epyk.core.js import expr


import config

# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

menu1 = rptObj.ui.div("menu 1", htmlCode="test_menu_1")
menu2 = rptObj.ui.div("menu2", htmlCode="test_menu_2")

menus = rptObj.ui.div([menu1, menu2])
menus.style.css.height = 0
menus.style.css.top = 0
menus.style.css.padding_bottom = 10
menus.style.css.border_bottom = '1px solid green'
menus.style.css.position = 'fixed'
for c in menus.components.values():
  c.style.css.display = False

divA = rptObj.ui.text("Test 1")
divB = rptObj.ui.text("Test 2")

menu_mapping = {divA: menu1, divB: menu2}

div = rptObj.ui.div([divA, divB], options={'inline': True})
for c in div.components.values():
  c.style.css.padding = "0 5px"

div.style.css.top = 0
div.style.css.position = 'fixed'
div.style.css.background = 'green'
div.style.css.color = 'white'
div.style.css.padding = '5px 0'


for menu_item, panel in menu_mapping.items():
  menu_item.click([
    std.querySelectorAll(std.selector(menus).with_child_element("div").excluding(panel)).css({"display": 'none'}),
    #
    expr.if_(std.querySelector(std.selector(menus)).getAttribute("data-panel") == menu_item.htmlCode, [
      std.querySelector(std.selector(menus)).setAttribute("data-panel", ""),
      std.querySelector(std.selector(menus)).css({"height": 0, "top": 0})
    ]).else_([
      std.querySelector(std.selector(menus)).setAttribute("data-panel", menu_item.htmlCode),
      std.querySelector(std.selector(menus)).css({"height": "auto", "top": "30px"})
    ]),
    std.querySelector(std.selector(panel)).css({'display': 'block'})
  ])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
