
import config

from epyk.core.Page import Report
from epyk.core.js import std

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

button1 = rptObj.ui.button("Button 1")
button2 = rptObj.ui.button("Button 1")
button3 =rptObj.ui.button("Button 1")


div1 = rptObj.ui.div("div 1")
div2 = rptObj.ui.div("div 2")
div3 = rptObj.ui.div("div 3")

div = rptObj.ui.div([div1, div2, div3])


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


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
