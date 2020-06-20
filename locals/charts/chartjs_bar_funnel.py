
from epyk.core.Page import Report

from epyk.tests import mocks


page = Report()
page.headers.dev()

page.ext_packages = {
  'funnel-chart-js': {
    'version': '1.1.2',
    'req': [{'alias': 'Chart.js'}],
    'website': 'https://material.io/components',
    'modules': [
      {'script': 'chart.funnel.min.js', 'path': 'funnel-chart-js/dist/'},
  ]}
}

c = page.ui.charts.chartJs.custom(mocks.languages, y_columns=["rating", 'change'], x_axis='name',
              options={"type": 'funnel', 'npm': 'funnel-chart-js', 'npm_path': r'C:\Angular\node_modules'})

