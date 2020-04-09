
from epyk.core.Page import Report

import config

rptObj = Report()


print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_codemirror"))
