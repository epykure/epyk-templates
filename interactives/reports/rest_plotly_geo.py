
import os

import config
from epyk.core.Page import Report


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

records = []

button = rptObj.ui.button("test")
europe = rptObj.ui.geo.plotly.choropleths.europe(records, size_col='size', country_col='countries')

button.click([
  rptObj.js.post("/data_plotly_geo").onSuccess([
    europe.build(rptObj.js.objects.data),
  ]),
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_INTERACTIVE, name=os.path.basename(__file__)[:-3])