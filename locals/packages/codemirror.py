
from epyk.core.Page import Report

import config

rptObj = Report()

# Console component
console = rptObj.ui.rich.console("This is a log section for all the events in the different buttons *", options={"timestamp": True})

css1 = rptObj.ui.codes.css('''
''')

# py1 = rptObj.ui.codes.python('''
# def test(a):
#   return a
# ''')

console.move()

rptObj.ui.button("Click").click([
  #css1.js.refresh(),
  css1.js.setOption("mode", 'css'),
  css1.js.refresh(),
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
