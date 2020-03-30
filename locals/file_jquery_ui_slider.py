
from epyk.core.Page import Report
from epyk.tests import data_urls

import config

rptObj = Report()


print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_jquery_ui_slider"))
