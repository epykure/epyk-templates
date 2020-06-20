
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()


input = page.ui.input(options={'reset': True})
container = page.ui.network.news() # options={"dated": False}
side = page.ui.navigation.side([container])
side2 = page.ui.navigation.side([])

button = page.ui.button("Add news")
button.click([
  container.build(input.dom.content)
])


replay = page.ui.button("Reset")
replay.click([
  container.js.reset(),

])
