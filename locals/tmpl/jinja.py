
from epyk.core.Page import Report


import config

rptObj = Report()
rptObj.headers.dev()

rptObj.ui.div("{{ name }}").css({"color": 'red'})

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)