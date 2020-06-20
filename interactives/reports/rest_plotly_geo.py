
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

records = []

button = page.ui.button("test")
europe = page.ui.geo.plotly.choropleths.europe(records, size_col='size', country_col='countries')

button.click([
  page.js.post("/data_plotly_geo").onSuccess([
    europe.build(page.js.objects.data),
  ]),
])
