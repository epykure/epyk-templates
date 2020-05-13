
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo


languages = [
  {"name": 'C', 'type': 'code', 'rating': 17.07, 'change': 12.82},
  {"name": 'Java', 'type': 'code', 'rating': 16.28, 'change': 0.28},
  {"name": 'Python', 'type': 'script', 'rating': 9.12, 'change': 1.29},
  {"name": 'C++', 'type': 'code', 'rating': 6.13, 'change': -1.97},
  {"name": 'C++', 'type': 'code', 'rating': 6.13, 'change': -1.97},
  {"name": 'C#', 'type': 'code', 'rating': 4.29, 'change': 0.3},
  {"name": 'Visual Basic', 'type': 'script', 'rating': 4.18, 'change': -1.01},
  {"name": 'JavaScript', 'type': 'script', 'rating': 2.68, 'change': -0.01},
  {"name": 'PHP', 'type': 'script', 'rating': 2.49, 'change': 0},
  {"name": 'SQL', 'type': 'script', 'rating': 2.09, 'change': -0.47},
  {"name": 'R', 'type': 'script', 'rating': 1.85, 'change': 0.90},
]


data_rest_1 = rptObj.py.requests.json(data_urls.PIVOTTABLE_DATA, store_location=r"C:\tmps")

# Create a table

tb1 = rptObj.ui.tables.pivots.ui(languages, ['name'], ['type'])
tb1.sub_total()

rptObj.ui.navigation.pilcrow()

tb2 = rptObj.ui.tables.pivots.plotly(data_rest_1, [], [])
#tb2.renderers.treemap()
#tb.aggregators.sum('change')
#tb.aggregators.max( 'change')
#tb.renderers.heatmap()

#rptObj.ui.button("Click").click([
#  tb.build(languages, options=tb.dom.options({'rows': ['type']}))
#])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)