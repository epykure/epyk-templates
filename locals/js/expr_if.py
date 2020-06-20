
from epyk.core.Page import Report
from epyk.core.js import expr


# Create a basic report object
page = Report()
page.headers.dev()

input = page.ui.input()

# Just generate a simple if statement on the value of the input
button = page.ui.button("Click Me").click([
  expr
    .if_(input.dom.content.number >= 10, [page.js.alert("Ok")])
    .elif_(input.dom.content == 'Other', [page.js.alert("Other")])
    .else_([page.js.alert("Else")
  ])
])

