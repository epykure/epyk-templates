
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()

# https://jsfiddle.net/djmartin_umich/9VJHe/
# http://dc-js.github.io/dc.js/vc/index.html


print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_geo_dc"))
