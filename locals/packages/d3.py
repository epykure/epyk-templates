
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()

csv = rptObj.js.d3.csv(data_urls.PLOTLY_APPLE_PRICES)

i = rptObj.ui.input()

rptObj.ui.button("click").click([
  csv.filterCol("direction", i.dom.content),
  rptObj.js.console.log(csv.unpack("test", "direction")),
  rptObj.js.console.log(i.dom.content)
])

data_rest_1 = rptObj.py.requests.csv(data_urls.DC_QUAKES, store_location=config.OUTPUT_TEMPS)

rptObj.ui.tables.d3.table(data_rest_1)

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
