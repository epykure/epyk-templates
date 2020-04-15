
import config
from epyk.core.Page import Report


# Create a basic report object
rptObj = Report()

top = rptObj.ui.banners.top("text")
top.style.css.height = 100
top.style.css.text_align = "center"
top.style.css.vertical_align = "middle"

#
icon = rptObj.ui.icon("fab fa-python")
text = rptObj.ui.text("This is a text")
bottom = rptObj.ui.banners.bottom([icon, text], options={"inline": True})

rptObj.ui.banners.corner("text", 'red')
rptObj.ui.banners.corner("text", 'red', position='top')

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)