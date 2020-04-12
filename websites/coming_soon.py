# https://www.w3schools.com/w3css/tryw3css_templates_coming_soon.ht

from epyk.core.Page import Report#

import config

rptObj = Report()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
