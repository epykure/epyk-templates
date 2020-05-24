import config

from epyk.core.Page import Report

rptObj = Report()

languages = [
  {"name": 'C', 'type': 'code', 'rating': 17.07, 'change': 12.82},
  {"name": 'Java', 'type': 'code', 'rating': 16.28, 'change': 0.28},
  {"name": 'Python', 'type': 'script', 'rating': 9.12, 'change': 1.29},
  {"name": 'C++', 'type': 'code', 'rating': 6.13, 'change': -1.97},
  {"name": 'C#', 'type': 'code', 'rating': 4.29, 'change': 0.3},
  {"name": 'Visual Basic', 'type': 'script', 'rating': 4.18, 'change': -1.01},
  {"name": 'JavaScript', 'type': 'script', 'rating': 2.68, 'change': -0.01},
  {"name": 'PHP', 'type': 'script', 'rating': 2.49, 'change': 0},
  {"name": 'SQL', 'type': 'script', 'rating': 2.09, 'change': -0.47},
  {"name": 'R', 'type': 'script', 'rating': 1.85, 'change': 0.90},
]


c = rptObj.ui.charts.chartJs.custom(languages, y_columns=["rating", 'change'], x_axis='name',
                                    options={"type": 'matrix', 'npm': 'chartjs-chart-matrix',
                                             'npm_path': r'C:\Angular\test-app\node_modules'})

c.plugins.zoom.zoom.enabled = True
c.plugins.zoom.zoom.mode = 'xy'
c.plugins.zoom.zoom.drag = True
c.plugins.zoom.pan.enabled = True
c.plugins.zoom.pan.mode = 'xy'

c.plugins.zoom.zoom.onZoom([
  rptObj.js.console.log("Test")
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
