
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()


# https://codepen.io/sgratzl/pen/qBWwxKP

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_geo_chartjs"))
