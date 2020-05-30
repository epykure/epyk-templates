
import config

from epyk.core.Page import Report
from epyk.tests import data_urls

# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

# Add a title to the report
rptObj.ui.title("Panel", level=3)

# Create a basic panel
title = rptObj.ui.title("Title")
slider = rptObj.ui.slider()
paragraph = rptObj.ui.texts.paragraph("This is a paragraph")
panel = rptObj.ui.layouts.panel([title, slider, paragraph])

# Change the style of the panel
panel.style.css.border = "1px solid grey"
panel.style.css.border_radius = "10px"
panel.style.css.padding = 10

# timer for color change onclick

# Add a title to the report
rptObj.ui.title("Sliding Panel", level=3)

# Create a sliding panel
paragraph2 = rptObj.ui.texts.paragraph("This is a paragraph")
sliding = rptObj.ui.panels.sliding([paragraph2], title="Title")
sliding.options.expanded = False

# Add extra HTML component to the sliding panel
paragraph3 = rptObj.ui.texts.paragraph("This is a paragraph 3")
sliding += paragraph3

# Add event on click on the sliding panel title bar
sliding.click([
  rptObj.js.console.log("This is a log")
])

# Add a title to the report
rptObj.ui.title("Split Panels", level=3)

# Create a split panel
left = rptObj.ui.col([
  rptObj.ui.div("left panel"),
  rptObj.ui.date(),
  rptObj.ui.fields.input(),
])

# Get data from a REST API
data_rest_1 = rptObj.py.requests.csv(data_urls.DC_QUAKES, store_location=config.OUTPUT_TEMPS)
right = rptObj.ui.col([
  rptObj.ui.div("right panel"),
  rptObj.ui.tables.d3.table(data_rest_1)
])

panel2 = rptObj.ui.panels.split(left, right)

# Add a title to the report
rptObj.ui.title("Drawers Panel", level=3)
# http://jsfiddle.net/KUCaL/


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
