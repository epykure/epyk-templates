
from epyk.core.Page import Report

from epyk.tests import mocks


# Create a basic report object
page = Report()
page.headers.dev()


a = page.ui.charts.chartJs.line(mocks.languages, y_columns=["rating", 'change'], x_axis='name')
a.dragData()
