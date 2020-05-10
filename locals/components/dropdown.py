
from epyk.core.Page import Report

import config

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

data = [
  {"value": 'value', 'items': [
      {"value": 'value 1'},
      {"value": 'value 2', 'items': [
        {"value": 'value 3'},
      ]},
  ]}
]

d = rptObj.ui.lists.dropdown(data)
d.click([
  rptObj.js.console.log(rptObj.js.objects.value)
])
rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
