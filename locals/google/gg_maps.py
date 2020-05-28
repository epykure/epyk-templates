
from epyk.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

# Enable Google Chart praduucst
rptObj.imports().google_products(['maps'])

map = rptObj.ui.geo.google.terrain(-33.92, 151.25)

rptObj.ui.button("Click").click([
  map.js.setMapTypeId('satellite'),
  map.js.setHeading(45),
])
#rptObj.ui.geo.google.current()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
