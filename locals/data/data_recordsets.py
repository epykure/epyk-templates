
from epyk.core.Page import Report

import config

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo


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

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
jsData = rptObj.data.js.record('data_test', languages)
filter = jsData.filterGroup("test")


rptObj.body.onReady([
  #
  #filter.equal('y', 25).startswith('text', 'test').setFilter("filterTest"),

  #rptObj.js.console.log(jsData.getFilter('filterTest')),
  #rptObj.js.console.log(jsData.getFilter('filterTest').group().count(["x", "y", "y1"], attrs={"name": 'ok'})),
  c.dom.write(filter.group().max("rating"), stringify=True),
  c.dom.write(filter.group().min("rating"), stringify=True),
  c.dom.write(filter.group().sortBy("change")[-1].defaults({"toto": 1}), stringify=True),
  c.dom.write(filter.group().pluck("name"), stringify=True),
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
