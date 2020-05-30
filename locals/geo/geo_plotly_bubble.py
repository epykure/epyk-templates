
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()
rptObj.headers.dev()


data_countries = rptObj.py.requests.csv(data_urls.PLOTLY_COUNTRIES, store_location=config.OUTPUT_TEMPS)

data_geo = rptObj.py.requests.csv(data_urls.GEO_US_CITIES, store_location=config.OUTPUT_TEMPS)

m = rptObj.ui.geo.plotly.bubbles.usa(data_geo, size_col='pop', long_col='lon', lat_col='lat', options={"scale": 50000, 'size': 1})

sa = rptObj.ui.geo.plotly.bubbles.south_america(data_countries, size_col='GDP (BILLIONS)', country_col='CODE')
w = rptObj.ui.geo.plotly.bubbles.world(data_countries, size_col='GDP (BILLIONS)', country_col='CODE')

rptObj.ui.row([w, sa])

records = [
  {'location': 'GBR', 'value': 40}
]
rptObj.ui.button("Click").click([
  #w.build(rptObj.data.plotly.locations(data_geo, 'location', 'value'))
  w.build(rptObj.data.plotly.locations(data_geo, 'lon', 'lat', 'pop'))
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
