
from epyk.core.Page import Report
from epyk.core.js import std


# Create a basic report object
page = Report()
page.headers.dev()

# Add a title to the report
page.ui.title("Events on the page", level=3)

# Trigger a function when a key is pressed on the page
page.ui.text("Press enter to display hello World")

# Add keyup event to the page itself
page.js.keyup.enter(std.alert('Hello World'))

# Add a title to the report
page.ui.title("Events on a component", level=3)
