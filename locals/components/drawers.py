
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()


button = page.ui.button("Test")

d = page.ui.drawer()
d.add_panel(page.ui.button("Test1"), "ok1")
d.add_panel(page.ui.button("Test2"), "ok2")
d.add_panel(page.ui.button("Test3"), "ok3")
d.set_handle(button)


d.drawers[0].click([
  d.dom.hide(),
  d.panels[0].dom.css({"display": 'block'}).r,
  page.js.console.log(d.dom.content)
])

d.drawers[1].click([
  d.dom.hide(),
  d.panels[1].dom.css({"display": 'block'}),
  d.dom.delete(1)
])

d.drawers[2].click([
  d.dom.hide(),
  d.panels[2].dom.css({"display": 'block'}).r])


d1 = page.ui.drawer()
d1.add_panel(page.ui.button("Test"), "ok")
d1.drawers[0].click([d1.panels[0].dom.css({"display": 'block'})])

page.ui.row([d, d1])

