
from epyk.core.Page import Report


# Defaults_css.Font.size = 20
# Create a basic report object
page = Report()
page.headers.dev()

button = page.ui.button("Go go Google")
button.goto("www.google.fr")


button2 = page.ui.button("Go go Google")
button2.goto("www.google.fr", name="_self")