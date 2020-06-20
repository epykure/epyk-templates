
from epyk.core.Page import Report
from epyk.core.js import expr
from epyk.core.js import std


# Create a basic report object
page = Report()
page.headers.dev()

input = page.ui.input()


while_lopp = expr.whileOf(input, options={"var": 'y'})
input.enter([
  std.console.log("Common for While"),
  std.var('ter', input.dom.content.number),
  expr.while_(std.var('ter') < 10).fncs([
    std.console.log(std.var("ter"))
  ]).next(std.var('ter') + 1),

  std.console.log("While loop on object items"),
  while_lopp.fncs([
    std.console.log(while_lopp.value)
  ]),

])

