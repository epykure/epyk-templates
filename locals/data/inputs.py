
from epyk.core.Page import Report


# Create a basic report object
page = Report(
  {'test': "this is a text",
   'test2': "this is a div"}
)
page.headers.dev()

page.ui.text(htmlCode="test")
page.ui.div(htmlCode="test2")

