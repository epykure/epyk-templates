
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()

data_geo = rptObj.py.requests.csv(data_urls.GEO_US_RAINS, store_location=config.OUTPUT_TEMPS)

#data_geo_covid = rptObj.py.requests.json(data_urls.TEST, store_location=config.OUTPUT_TEMPS)
#print(data_geo_covid)

#
# data_meteo_usa_path = 'https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv'
# data_meteo_usa_path = 'https://raw.githubusercontent.com/plotly/datasets/master/2015_06_30_precipitation.csv'
# data_geo = rptObj.py.requests.csv(data_meteo_usa_path)
# print(data_geo)
#

# gs = rptObj.ui.geo.plotly.scatter([])
# d = rptObj.ui.geo.plotly.density([])

m = rptObj.ui.geo.plotly_bubble.usa(data_geo[:20], lon_columns=['Lon'], lat_columns=['Lat'])
m.data.locations = ['FRA', 'DEU', 'RUS', 'ESP']
m.data.marker.size = [20, 30, 15, 10]
m.data.marker.color = [10, 20, 40, 50]

#scmb = rptObj.ui.geo.plotly.scattermapbox(data_geo, lon_columns=["Longitude"], lat_columns=["Latitude"])
#scmb.layout.no_background()

#scgeo = rptObj.ui.geo.plotly.bubble('usa', data_geo, y_column="lon", x_axis="lat")
#scgeo.data.locationmode = 'USA-states'
#scgeo.layout.no_background()

data = []
#rptObj.ui.geo.plotly.bubble('europe', data, y_column='v', x_axis='i')
#rptObj.ui.geo.plotly.asia(data, y_column='v', x_axis='c')
#af = rptObj.ui.geo.plotly.africa(data, y_column='v', x_axis='c')
#us = rptObj.ui.geo.plotly.usa(data, y_column='v', x_axis='c')

#af.data.zmin = 500
#af.data.zmax = 500

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
