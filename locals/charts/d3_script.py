
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

page.ui.charts.d3.cloud("This sn example of text in the world cloud")
page.ui.charts.d3.cloud("This is a second example ")

