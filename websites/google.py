from epyk.core.Page import Report#

import config

rptObj = Report()
rptObj.body.style.css.padding = "0 50px"

results = [
  {"title": 'Packaging Python Projects — Python Packaging User Guide',
   'urlTitle': '#',
   'icon': '',
   'url': '#',
   'dsc': 'Creating setup.py¶. setup.py is the build script for setuptools. It tells setuptools about your package (such as the name and ...'},
  {"title": 'Window.open() - Web APIs | MDN',
   'urlTitle': 'https://developer.mozilla.org/en-US/docs/Web/API/Window/open',
   'dsc': "19 Mar 2020 - The Window interface's open() method loads the specified resource into the new or existing browsing context (window, or tab) with the specified name. If the name doesn't exist, then a new browsing context is opened in a new tab or a new window, and the specified resource is loaded into it."},
]

rptObj.ui.rich.search_input()
rptObj.ui.rich.search_results(results)

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
