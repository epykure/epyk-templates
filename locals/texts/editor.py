
from epyk.core.Page import Report


page = Report()
page.headers.dev()

# Console component
console = page.ui.rich.console("This is a log section for all the events in the different buttons *", options={"timestamp": True})

# c = page.ui.inputs.cell("")
# c.run([])
# c.save([])

# e = page.ui.inputs.editor("print('test')")
# e.action("fas fa-share-alt", [])
# e.clear([])
# e.run([
#   e.textarea.dom.setOption('mode', 'python'),
#   e.textarea.dom.clear(),
#   e.dom.timestamp(),
#   console.dom.write(e.textarea.dom.content)
# ])
# e.toggle([])
# e.copy([], tooltip="Copy Code")

# page.ui.button("Click").click([
#   c.textarea.js.setSize(height=40)
#   #t.dom.append("# hello, markdown!"),
#   #t.dom.empty(),
#   #console.dom.write(t.dom.content)
# ])

console.move()

