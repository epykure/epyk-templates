
import config
from epyk.core.Page import Report


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()


danger = rptObj.ui.network.warning()

button = rptObj.ui.button("Show")
button.click([
  danger.build('''
  ###New 
alert
  ''')
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)