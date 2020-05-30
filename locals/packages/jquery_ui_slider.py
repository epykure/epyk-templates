
from epyk.core.Page import Report

import config

rptObj = Report()
rptObj.headers.dev()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})


s1 = rptObj.ui.slider(40)
s1.options.max = 300

s2 = rptObj.ui.slider(40)
s2.options.disabled = True

#
row = rptObj.ui.row([
  s1, s2
])

# Create a simple slider
s3 = rptObj.ui.slider(40)
s3.change([
  c.dom.write(s3.dom.content),
]).css({"margin-bottom": "5px"})

# Add a slider based on a range of numbers
s4 = rptObj.ui.sliders.range([12, 546, 98])

rptObj.ui.layouts.hr()

# Set a slider of dates
s5 = rptObj.ui.sliders.date("2020-01-02", min="2020-01-01", max="2020-12-31")
s5.options.range = "min"

rptObj.ui.layouts.hr()

# Set a slider for a range of dates
s6 = rptObj.ui.sliders.date_range("2020-01-02", "2020-06-02", min="2020-01-01", max="2020-12-31")

for col in row:
  col.css({"padding": '5px'})

# Add event on the progress bar to change and retrieve the value
rptObj.ui.button("click").click([
  c.dom.write(s1.dom.content),
  c.dom.write(s4.dom.content),
  c.dom.write(s5.dom.content),
  c.dom.write(s2.dom.val, stringify=True),
])

rptObj.ui.button("Enable").click([
  s2.js.enable(),
  c.dom.write(s6.dom.content),
])

rptObj.ui.button("Set 150").click([
  s1.build(150)
])

c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
