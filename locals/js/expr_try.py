
import config

from epyk.core.Page import Report

from epyk.core.js import expr
from epyk.core.js import std


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

input = rptObj.ui.input()


# Simple try except example
input.enter([
  expr
    .try_(input.dom.content.number.toPrecision(500))
    .catch([std.console.log("Error raised precision too large")
  ])
])


input2 = rptObj.ui.input()
input2.enter([
  # Alway raise an exception
  expr.throw("Error! Error!")
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
