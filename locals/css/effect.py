
import config

from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

# Dom events are available on each components and they will be more detailed on the Javascript section
# CSS effects are mainly driven by Javascript function
div = rptObj.ui.div("This is a text")
div.style.css.cursor = 'pointer'

div.click([
  # Change the color to red for 1 second
  div.dom.transition("color", "red", duration=1, reverse=True)
])

# CSS animate can also be done using transition effects
# There is a catalog of predefined effects
div = rptObj.ui.div("This is a new text")
div.style.effects.blink(2)

# it possible to define a custom animation
div = rptObj.ui.div("This is a animated text")
div.style.effects.animate('test - animate', {"color": "red", "padding-left": "200px"}, delay=5, iteration_count=False)

# Adding classes to the framework
from epyk.core.css.styles.classes import CssStyle


class CssHoverColor(CssStyle.Style):
  _attrs = {'color': 'blue', 'cursor': 'pointer'}
  _hover = {'color': 'orange'}


# Bespoke component creation
div_a = rptObj.ui.div("Div with shared class")
div_b = rptObj.ui.div("Div with shared class")

div_a.style.add_classes.custom(CssHoverColor)
div_b.style.add_classes.custom(CssHoverColor)

# Overriding advances CSS attributes (hover, focus, after, before)
# This will create a CSS class for the component and it will add all the inline CSS definition to it automatically
# The style attribute of the component will then be empty
div = rptObj.ui.div("This is a text with an interactive style")
div.style.css.padding = 10
div.style.hover({"color": 'green'})

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)