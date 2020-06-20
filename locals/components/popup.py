
from epyk.core.Page import Report

# Using data and JavaScript shortcuts
from epyk.core.js import std
from epyk.core.data import events


# Create a basic report object
page = Report()
page.headers.dev()

div = page.ui.div("Test")
div.style.css.background = 'white'

button = page.ui.button("show")
popup = page.ui.layouts.popup([div], options={"background": False, 'draggable': True})

button.click([
  popup.dom.show()
])

