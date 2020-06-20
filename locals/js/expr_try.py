
from epyk.core.Page import Report

from epyk.core.js import expr
from epyk.core.js import std


# Create a basic report object
page = Report()
page.headers.dev()

input = page.ui.input()


# Simple try except example
input.enter([
  expr
    .try_(input.dom.content.number.toPrecision(500))
    .catch([std.console.log("Error raised precision too large")
  ])
])


input2 = page.ui.input()
input2.enter([
  # Alway raise an exception
  expr.throw("Error! Error!")
])

