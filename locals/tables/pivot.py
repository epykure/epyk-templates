
from epyk.core.Page import Report

from epyk.tests import data_urls
from epyk.tests import mocks


# Create a basic report object
page = Report()
page.headers.dev()

data_rest_1 = page.py.requests.json(data_urls.PIVOTTABLE_DATA)

# Create a table

tb1 = page.ui.tables.pivots.ui(mocks.languages, ['name'], ['type'])
tb1.sub_total()

page.ui.navigation.pilcrow()

tb2 = page.ui.tables.pivots.plotly(data_rest_1, [], [])
#tb2.renderers.treemap()
#tb.aggregators.sum('change')
#tb.aggregators.max( 'change')
#tb.renderers.heatmap()

#page.ui.button("Click").click([
#  tb.build(languages, options=tb.dom.options({'rows': ['type']}))
#])
