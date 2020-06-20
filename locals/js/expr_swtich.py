
from epyk.core.Page import Report

from epyk.core.js import expr
from epyk.core.js import std


# Create a basic report object
page = Report()
page.headers.dev()

slider = page.ui.slider()


slider.change([
  expr.switch(slider)
    .caseAbove(25, [std.alert("Above 25")])
    .caseRange(10, 24, [std.alert(slider.dom.content)])
    .caseBelow(10, [std.alert("Below 10")], include_value=False)
])
