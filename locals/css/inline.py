
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

# Create component
div = page.ui.div("This is a container 1")

# Get the default CSS styles
# print(div.style.css)

# Change the CSS Style
# all the CSS properties are available and are documented
div.style.css.color = "red"
div.style.css.display = "inline-block"
div.style.css.width = "auto"

# Those inline CSS properties will override the ones defined in the CSS classes
# The below method will return the CSS classes defined in this component
# The main will be added to it whereas the other will only be added to the page
# print(div.style.get_classes())

# using a Jquery like function
div.css({"border": '1px solid black'})

# Remove the CSS style for the defined component
cont = page.ui.div("This is a container 2")
cont.style.clear_style()
# print(div.style.css)

# change the Framework default styles
from epyk.core.css import Defaults

# Since this point the default values will be changed and the components will use then to get their styles
Defaults.Font.size = 20

div2 = page.ui.div("This is a container 3")

# Some functions are available to avoid changing the common reference
div3 = page.ui.div("This is a container 4")
div3.style.css.font_size = Defaults.font(-5) # -5 from the reference

# Reset the default size to not corrupt the other reports
Defaults.Font.size = 12