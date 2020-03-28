import sys
sys.path.append("../../epyk-ui")

from epyk.core.Page import Report
from epyk.tests import data_urls

import config

# Create a basic report object
rptObj = Report()

data_rest_1 = rptObj.py.requests.csv(data_urls.DC_QUAKES, store_location=r"C:\tmps")

# http://bl.ocks.org/d3noob/6077996
#data_rest_2 = rptObj.py.requests.csv(data_urls.AIRPORT_TRAFFIC, store_location=r"C:\tmps")

# Main cross filter object
crossfilter = rptObj.js.data.crossfilter(data_rest_1, "test")
dimension = crossfilter.dimension([('phases', str), ('magnitude', int)], 'test_dim')

# Sub dimension
d2 = rptObj.js.data.crossfilter(crossDimension=dimension.filterOnColumn("15", 'phases'), var_name="test_2")
dimension2 = d2.dimension([('agency', str), ('magnitude', int)], 'test_dim_2')
group = dimension2.group('group_name') # groupFunction('test_3', 'function(total) { return total[0] }')


d3 = rptObj.js.data.crossfilter(crossDimension=dimension.filterOnColumn("24", 'phases'), var_name="test_3")
dimension3 = d3.dimension([('agency', str), ('magnitude', int)], 'test_dim_3')
group3 = dimension3.GroupAll('group_name_3') # groupFunction('test_3', 'function(total) { return total[0] }')

rptObj.body.onReady([
  crossfilter, dimension, d2, dimension2, group,
  d3, dimension3, group3,

  rptObj.js.console.log(group.reduceSum('magnitude').all()),
  rptObj.js.console.log(dimension3.top()),
])

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_data_crossfilter"))
