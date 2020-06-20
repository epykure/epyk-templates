
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

# Enable Google Chart praduucst
page.imports().google_products(['maps'])

map = page.ui.geo.google.terrain(-33.92, 151.25)

page.ui.button("Click").click([
  map.js.setMapTypeId('satellite'),
  map.js.setHeading(45),
])
#page.ui.geo.google.current()
