
from epyk.core.Page import Report

from epyk.tests import mocks


page = Report()
page.headers.dev()

c = page.ui.charts.chartJs.custom(mocks.languages, y_columns=["rating", 'change'], x_axis='name',
                                    options={"type": 'pcp', 'npm': 'chartjs-chart-pcp',
                                             'script': 'Chart.PCP',
                                             'npm_path': r'C:\Angular\test-app\node_modules'})


