
from epyk.core.Page import Report
from epyk.tests import data_urls


# Create a basic report object
page = Report()
page.headers.dev()

data_rest_1 = page.py.requests.csv(data_urls.DC_QUAKES)

# http://bl.ocks.org/d3noob/6077996
#data_rest_2 = page.py.requests.csv(data_urls.AIRPORT_TRAFFIC, store_location=r"C:\tmps")

# Main cross filter object
crossfilter = page.js.data.crossfilter(data_rest_1, "test")
dimension = crossfilter.dimension([('phases', str), ('magnitude', int)], 'test_dim')

# Sub dimension
d2 = page.js.data.crossfilter(crossDimension=dimension.filterOnColumn("15", 'phases'), var_name="test_2")
dimension2 = d2.dimension([('agency', str), ('magnitude', int)], 'test_dim_2')
group = dimension2.group('group_name') # groupFunction('test_3', 'function(total) { return total[0] }')


d3 = page.js.data.crossfilter(crossDimension=dimension.filterOnColumn("24", 'phases'), var_name="test_3")
dimension3 = d3.dimension([('agency', str), ('magnitude', int)], 'test_dim_3')
group3 = dimension3.GroupAll('group_name_3') # groupFunction('test_3', 'function(total) { return total[0] }')

page.body.onReady([
  crossfilter, dimension, d2, dimension2, group,
  d3, dimension3, group3,

  page.js.console.log(group.reduceSum('magnitude').all()),
  page.js.console.log(dimension3.top()),
])

