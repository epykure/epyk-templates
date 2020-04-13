
import config

from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()

# https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css
rptObj.css.customFile("animate.min.css", path="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2")

# Add the file from the local environment context defined in Imports.STATIC_PATH
# This path will be overridden and specific to your configuration
rptObj.css.customFile("test.css")

# Create CSS text fragments to be added to the final HTML page
rptObj.css.customText('''
.red_color {
  color: red
 }
''')

# Bespoke component creation
t = rptObj.ui.text("test")

# Attach the bespoke CSS class deduced from the text fragment
t.style.add_classes.external("red_color")

# Basic library use
# more details here: https://github.com/daneden/animate.css#Basic-Usage
t2 = rptObj.ui.text("test")

# Attach a CSS class from the animate.min.css module
t2.style.add_classes.external(["animated", "bounce"])

# Create a bespoke CSS class from the Python framework
# => target being to get this included at some point in the official package
from epyk.core.css.styles.classes import CssStyle


class CssHoverColor(CssStyle.Style):
  _attrs = {'color': 'blue', 'cursor': 'pointer'}
  _hover = {'color': 'orange'}

# Bespoke component creation
div = rptObj.ui.div("This is a container")

# Attach the class to the component
div.style.add_classes.custom(CssHoverColor)

class CssBodyMargin(CssStyle.Style):
  _attrs = {'padding': '0 40px'}

# same thing can be added to the body
rptObj.body.style.add_classes.custom(CssBodyMargin)

# it is important to keep in mind that the inline CSS style of any component will be used in priority compoared
# to the styles in a CSS class
v_cls = rptObj.css.anonymous_cls({
  '_attrs': {'color': 'green', 'cursor': 'pointer'},
  '_hover': {'color': 'red'}})

# Bespoke component creation
div2 = rptObj.ui.div("This is a container")
div2.style.add_classes.custom(v_cls)

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
