
from epyk.core.Page import Report
from epyk.core.js import std


# Create a basic report object
page = Report()
page.headers.dev()

button1 = page.ui.button("Button 1")
button2 = page.ui.button("Button 1")
button3 =page.ui.button("Button 1")


div1 = page.ui.div("div 1")
div2 = page.ui.div("div 2")
div3 = page.ui.div("div 3")

div = page.ui.div([div1, div2, div3])


button1.click([
  std.querySelectorAll(std.selector(div).with_child_element("div").excluding(div1)).css({"display": 'none'}),
  std.querySelector(std.selector(div1)).css({"display": 'block'})
])

button2.click([
  std.querySelectorAll(std.selector(div).with_child_element("div").excluding(div2)).css({"display": 'none'}),
  std.querySelector(std.selector(div2)).css({"display": 'block'})
])

button3.click([
  std.querySelectorAll(std.selector(div).with_child_element("div").excluding(div3)).css({"display": 'none'}),
  std.querySelector(std.selector(div3)).css({"display": 'block'})
])

