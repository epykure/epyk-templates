
import config
from epyk.core.Page import Report


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

# Add a banner on top of the page
top = rptObj.ui.banners.top("text")
top.style.css.font_size = '40px'

# Change the banner style
top.style.css.height = 100
top.style.css.text_align = "center"
top.style.css.vertical_align = "middle"

# Add a banner with HTML content
icon = rptObj.ui.icon("fab fa-python")
text = rptObj.ui.text("This is a text")

# Chang the option to have the content in one line
bottom = rptObj.ui.banners.bottom([icon, text], options={"inline": True})

# Add a banner on the bottom right corner
b = rptObj.ui.banners.corner("bottom", 'red')
# Add click event on the banner
b.click([
  # hide the bonner on click
  b.dom.hide()
])

# Add a banner on the top right conner
conrner = rptObj.ui.banners.corner("top", 'red', position='top')
# Add interactivity on the banner style
conrner.style.hover({"background": "white", 'color': 'red'})

# Add event when mouse is on the component
conrner.hover([
  # display the banner
  b.dom.show()
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)