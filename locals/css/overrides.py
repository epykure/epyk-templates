
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

# Framework is quite flexible and most of the attributes can be changed and overridden before transpiling to Javascript.
# This section will just remind some overrides already mentioned in some other examples
# Everything related to the report styling can be overridden until the end (and only the last value will remain).

# In the below Example only the green color will be written to the page
div1 = page.ui.div("This is a text 1")
div1.style.css.color = "red"
div1.style.css.color = "green"
