
from epyk.core.Page import Report

import config

rptObj = Report()

# Console component
console = rptObj.ui.rich.console("This is a log section for all the events in the different buttons *", options={"timestamp": True})

# c = rptObj.ui.inputs.cell("")
# c.run([])
# c.save([])

# e = rptObj.ui.inputs.editor("print('test')")
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

# t = rptObj.ui.inputs.textarea("Test", placeholder='This is a placeholer')
# t.selectable()
# t.options.rows = 10
# print(t.attr)


# rptObj.ui.button("Click").click([
#   c.textarea.js.setSize(height=40)
#   #t.dom.append("# hello, markdown!"),
#   #t.dom.empty(),
#   #console.dom.write(t.dom.content)
# ])


#console.move()

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_codemirror"))
