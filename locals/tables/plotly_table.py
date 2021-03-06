
from epyk.core.Page import Report
from epyk.core.css import Colors

from epyk.tests import data_urls


# Create a basic report object
page = Report()
page.headers.dev()

page.body.set_background()

data_rest_1 = page.py.requests.csv(data_urls.DC_QUAKES)

# Create a table
tb = page.ui.tables.plotlys.table(data_rest_1, ['agency', 'origintime'], ['longitude', 'latitude'])

# Create a second table based on the same dataset but with different columns
tb2 = page.ui.tables.plotlys.table(data_rest_1, ['status', 'phases', 'origin_geom'], ['longitude', 'latitude', 'depth'])

# Change the color of the first column
# and remove the background for the other columns
tb2.columns_color(["red", Colors.RgbColors.TRANSPARENT])

# Change the header color
tb2.headers_color(['black'])
tb2.headers_font_color(['white'])
