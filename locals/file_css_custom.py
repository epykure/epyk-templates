
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


print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_css_custom"))
