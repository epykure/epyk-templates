
from epyk.core.Page import Report
from epyk.core.js import expr
from epyk.core.js import std

# Create a basic report object
page = Report()
page.headers.dev()

input = page.ui.input()


input.enter([
  std.console.log("Common for loop"),
  expr.for_(input).fncs([
    std.console.log(std.var("i"))
  ]),

  std.console.log("For loop on object properties"),
  expr.forIn(input).fncs([
    std.console.log(std.var("x"))
  ]),

std.console.log("For loop on object items"),
  expr.forOf(input, options={"var": 'y'}).fncs([
    std.console.log(std.var("y"))
  ]),
])

