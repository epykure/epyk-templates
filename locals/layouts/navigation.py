
import config
from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

rptObj.ui.layouts.new_line(20)
rptObj.ui.button("Click").click([
  rptObj.js.alert(rptObj.js.window.scrollPercentage)
])

rptObj.ui.layouts.new_line(20)

rptObj.ui.button("Click 2").click([
  rptObj.js.alert(rptObj.js.window.scrollPercentage)
])

rptObj.ui.layouts.new_line(20)

rptObj.ui.button("Click 3").click([
  rptObj.js.alert(rptObj.js.window.scrollPercentage)
])


rptObj.ui.layouts.new_line(20)

rptObj.ui.button("Click 4").click([
  rptObj.js.alert(rptObj.js.window.scrollPercentage)
])

rptObj.ui.layouts.new_line(20)

p = rptObj.ui.navigation.scroll(60)

#rptObj.ui.sliders.progressbar(0, height=(5, 'px'))

# rptObj.js.addOnReady(
#   rptObj.js.window.events.addScrollListener([
#     p.build(rptObj.js.window.scrollPercentage)
# ]))

# p.style.css.fixed_top()
p.style.css.fixed_top()

rptObj.ui.button("Click 5").click([
  p.build(rptObj.js.window.scrollPercentage)
])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
