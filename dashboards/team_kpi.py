
from epyk.core.Page import Report


# Create a basic report object
page = Report()

page.ui.text("#This is a text", options={"markdown": True})

test = page.ui.icons.date("2020-09-24")
test.select([
  page.js.console.log(test.input.dom.content)]
)

