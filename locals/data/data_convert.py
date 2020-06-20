
from epyk.core.Page import Report
from epyk.core import data

from epyk.tests import mocks


# Create a basic report object
page = Report()
page.headers.dev()

#
result = data.plotly.surface(mocks.languages, y_columns=['rating'], x_axis="change", z_axis="change")

nvd3 = data.c3.y(mocks.languages, y_columns=['change'], x_axis="name")

#print(result)
# print(data_rest)