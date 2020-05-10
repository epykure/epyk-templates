##

from epyk.core.Page import Report
from epyk.tests import data_urls

import config

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# retrieve some random json data
data_rest = rptObj.py.requests.csv(data_urls.BLOG_OBJECT, store_location=config.OUTPUT_TEMPS)

# create a json viewer object
j = rptObj.ui.json(data_rest, height=(100, 'px'))

# change the default options
j.options.open = False
j.options.hoverPreviewEnabled = True

# add a button for interactivity
rptObj.ui.button("Click").click([
  j.js.openAtDepth(0),
  j.build({"test": 'ok'})
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
