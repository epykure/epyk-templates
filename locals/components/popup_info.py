

from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

input = page.ui.input(htmlCode="test")

message = page.ui.texts.note("Some text...", "Success")
message.style.css.display = False
page.ui.button("Click").click([
  message.build(input.dom.content),
  message.dom.show(duration=5)
])