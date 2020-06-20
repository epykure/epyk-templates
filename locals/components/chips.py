
from epyk.core.Page import Report


page = Report()
page.headers.dev()

# Console component
c = page.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
ch = page.ui.chips(["example", {"value": 'test', 'name': 'group 2'}], options={"visible": True})
ch.append("new data")
ch.enter([

])

ch.keyup.shift_with('L',[
  page.js.alert("Ok")
])

page.ui.button('Click').click([
  ch.dom.add(ch.dom.input),
  c.dom.write(ch.dom.content)
])

#
page.ui.button('Add Fixed').click([
  ch.dom.add(ch.dom.input, category="other", fixed=True),
  c.dom.write(ch.dom.content, stringify=True),
  c.dom.write(ch.dom.values('group')),
  c.dom.write(ch.dom.values()),
])

#
icons = page.ui.icons.bar(['fas fa-times', 'fas fa-anchor'])
icons[0].click([
  page.js.alert("pl")
])
c.move()

# print( page.imports().show(all=True))


