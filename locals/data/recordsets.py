
from epyk.core.Page import Report

import config

# Create a basic report object
rptObj = Report()

rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

dataPoints = [
  {'x': 0, 'y': 10, 'y1': 10, 'text': 'test 1'},
  {'x': 1, 'y': 25, 'text': 'test 2'},
  {'x': 2, 'y': 25, 'y1': 10, 'text': 'case 1'},
  {'x': 1, 'y': 25, 'y1': 5, 'text': 'test 3'},
  {'x': 4, 'y': 2, 'y1': 10, 'text': 'case 3'}]

input = rptObj.ui.input()

jsData = rptObj.data.js('data_test', dataPoints)
filter = jsData.filterGroup("test")

rptObj.body.onReady([
  #
  filter.equal('y', 25).startswith('text', 'test').setFilter("filterTest"),

  rptObj.js.console.log(jsData.getFilter('filterTest')),
  rptObj.js.console.log(jsData.getFilter('filterTest').group().count(["x", "y", "y1"], attrs={"name": 'ok'})),
  # '''function filterOption2(r, k, v){var n=[];r.forEach(function(e){if(e[k]==v){n.push(e)}});return n};
  # ''',
  # '''
  # var dataPoints = [
  # {'x': 0, 'y': 10, 'y1': 10},
  # {'x': 1, 'y': 35, 'y1': 20},
  # {'x': 2, 'y': 25, 'y1': 10},
  # {'x': 3, 'y': 30, 'y1': 5},
  # {'x': 4, 'y': 28, 'y1': 10}]
  #
  # ''',
  # 'console.log( filterOption(dataPoints, ["y"], "x") )',
  #rptObj.js.console.log("dataPoints", skip_data_convert=True)
  #js_data.clearFilters()
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
