
import config

from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

div = rptObj.ui.div("This is a text")

# Classlist like feature to access all the classes loaded for a given object
# Classes are not supposed to be changed and they are properties shared across components
for label, sections in div.style.classList.items():
  rptObj.ui.title(label, 3)
  for v in sections:
    rptObj.ui.text(v)

# All the classes in the framework are located in the catalog in the style property using add_classes
div.style.add_classes.text.colored()
for label, sections in div.style.classList.items():
  rptObj.ui.title(label, 3)
  for v in sections:
    rptObj.ui.text(v)

#
# Create a bespoke CSS class from the Python framework
# => target being to get this included at some point in the official package
from epyk.core.css.styles.classes import CssStyle


class CssHoverColor(CssStyle.Style):
  _attrs = {'color': 'blue', 'cursor': 'pointer'}
  _hover = {'color': 'orange'}


div1 = rptObj.ui.div("This is a text")
# Attach the class to the component
div1.style.add_classes.custom(CssHoverColor)

# Example of use of data content to fill a CSS attribute
div = rptObj.ui.div("")
div.style.attr_content("data-content")
div.attr["data-content"] = 'blue'

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
