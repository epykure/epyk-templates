
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

i = page.ui.fields.input("", label="Range Example", icon="fas fa-unlock-alt")
#i.dom.animate("transform", "rotate", "0 190 50", "360 190 50")

page.ui.button("test").click([
  i.label.dom.transition('margin-left', '100px', 2, reverse=True),
  i.label.dom.transition('color', 'red', 5, reverse=True),
  #i.label.dom.css({'WebkitTransition': 'opacity 1s'}),
  #i.label.dom.transform.translateX(100),
  #i.label.dom.transform.skewX(20),
  #i.label.dom.transform.rotate(90),
  #page.js.alert("ok"),
])

