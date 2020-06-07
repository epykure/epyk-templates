
from epyk.core.Page import Report


import config

# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

nav = rptObj.ui.panels.nav(options={"position": 'bottom'})
nav.add_panel("Test", rptObj.ui.div("Container"))
nav.add_panel("Test 2", rptObj.ui.div("Container 2"))

rptObj.ui.div([nav]).css({'border': '1px solid black', 'height': '200px'})

nav2 = rptObj.ui.navigation.panel()
nav2.add_panel("Test", rptObj.ui.div("Container"))
nav2.add_panel("Test 2", rptObj.ui.div("Container 2"))

rptObj.ui.div([nav2]).css({'border': '1px solid black', 'height': '200px'})

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
