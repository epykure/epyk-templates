
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# https://jsfiddle.net/djmartin_umich/9VJHe/
# http://dc-js.github.io/dc.js/vc/index.html


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
