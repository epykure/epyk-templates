
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()
rptObj.headers.dev()


# https://codepen.io/sgratzl/pen/qBWwxKP

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)