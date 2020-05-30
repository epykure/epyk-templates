
from epyk.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()


# rptObj.ui.forms.inputs([
#   {"label": "name", "htmlCode": "input"},
#   {"label": "name 2", "htmlCode": "input2"},
# ]) # , "http://127.0.0.1:5000", "POST"

t = rptObj.ui.text("youpi").editable()
#r = rptObj.ui.select([
#  {"name": 'Test', 'value': "false"},
#  {"name": 'Test 2', 'value': "true"},
#])

#rptObj.ui.button("Test").click([
#  rptObj.js.console.log(r.dom.val),
#  t.dom.contentEditable(r.dom.content)
#])

#print(rptObj.ui.text("youpi").dom.contentEditable(True))
#rptObj.ui.forms.date("http://127.0.0.1:5000", "POST")
#rptObj.ui.forms.dates("http://127.0.0.1:5000", "POST")
b = rptObj.ui.button("Run").css({"width": "100px"})

#s = rptObj.ui.select(["A", "B"])
n = rptObj.ui.layouts.new_line()
#s.set_attrs({"name": "ok"})
#f = rptObj.ui.layouts.form([n])
#f += f.submit

b.click([
  rptObj.js.console.log(rptObj.js.objects.mouseEvent.offsetX),
  rptObj.js.console.log(rptObj.js.objects.mouseEvent.getField("type"))
])

#popup = rptObj.ui.layouts.popup(rptObj.ui.title('Test'), color="red")
#popup + rptObj.ui.texts.paragraph('Test')

# rptObj.ui.forms.input("")

# popup = rptObj.ui.layouts.popup(rptObj.ui.title('Test'), color="red")
# popup + rptObj.ui.texts.paragraph('Test')

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)


# rptObj.py.requests.http_server(5000)