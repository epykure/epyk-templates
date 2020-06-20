
from epyk.core.Page import Report

from epyk.tests import mocks


page = Report()
page.headers.dev()

data_series = mocks.getSeries(5, 30)

sur = page.ui.charts.plotly.surface(data_series, y_columns=[1], x_axis='x', z_axis=2)
