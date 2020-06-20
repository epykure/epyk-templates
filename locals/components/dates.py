
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

page.ui.date()
page.ui.fields.today()

page.ui.button("Click").click([

])
