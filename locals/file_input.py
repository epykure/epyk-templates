
import config
from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()

input = rptObj.ui.inputs.d_range(3)
text_area = rptObj.ui.inputs.textarea("This is a textarea")


contents = rptObj.ui.contents()
#
rptObj.ui.title("title")
# rptObj.ui.title("title", level=2, contents=contents)
# rptObj.ui.title("title", contents=contents)
#
# number = rptObj.ui.rich.number(500, "Test", height=(150, 'px'))
# number.add_label("This is a first **label** to be checked", position="after", css={"margin": 0})
# number.label.add_options({"css": {"color": 'red'}})
# number.span.add_icon(rptObj.ui.icons.get.ICON_ENVELOPE)
#
# rptObj.ui.layouts.div([
#   rptObj.ui.div("Test", width=("100", "px"), htmlCode="test").css({"border": '1px solid black', 'display': 'inline-block'}),
#   rptObj.ui.div("Test2", width=("100", "px")).css({"border": '1px solid black', 'display': 'inline-block'}),
#   rptObj.ui.div("Test3", width=("100", "px"), htmlCode="test3").css({"border": '1px solid black', 'display': 'inline-block'}),
#   rptObj.ui.div("Test4", width=("100", "px")).css({"border": '1px solid black', 'display': 'inline-block'}),
#   rptObj.ui.div([
#     rptObj.ui.rich.number(100, "Number"),
#     rptObj.ui.rich.prism("print('test')"),
#   ], htmlCode="content").css({'display': 'none'}),
#   rptObj.ui.div("Test4", htmlCode="content2").css({'display': 'none'}),
# ], width=("auto", ""))
#

# rptObj.ui.options_bar([
#   {"icon": "fab fa-accusoft"},
#   {"icon": "fab fa-accusoft"},
# ]).draggable()
#

data = [{"value": 'test', '_children': [
  {"label": 'child 1', 'color': 'red', 'value': 'red'},
  {"label": 'child 1', 'color': 'red', 'value': 'blue'}
]},{
   "value": 'prog', '_children': [
    {'value': 'python'},
  ]
         }]

rptObj.ui.texts.number(28, title="Total RFQs", color="green")
rptObj.ui.texts.number(9, title="Working", color="orange")
rptObj.ui.texts.number(4, title="Done", color="green")
rptObj.ui.texts.number(15, title="Missed", color="red")


# w = rptObj.ui.workflow([
#   {"value": 'test 1', "status": 'success', 'label': 'test'},
#   {"value": 'test 1', "status": 'success'},
#   {"value": 'test 1', "status": 'success'},
#   {"value": 'test 1', "status": 'success'},
#   {"value": 'test 1', "status": 'pending'},
#   {"value": 'test 1'},
#   {"value": 'test 1'},
#   {"value": 'test 1'},
# ])

# rptObj.ui.button("worklow").click([
#   w.dom.set_complete(5)
# ])


rptObj.ui.row([
  rptObj.ui.title("test"),
  rptObj.ui.col([
    rptObj.ui.rich.light("red", label="test", tooltip="Test"),
    rptObj.ui.rich.light(True, label="test"),
    rptObj.ui.rich.light(False, label="test"),
    rptObj.ui.fields.now(label="test")
  ])
])

rptObj.ui.fields.now(label="test")
rptObj.ui.fields.cob(label="test")

i = rptObj.ui.fields.static(label="test", value="Test 2", placeholder="Read only", helper="RRRR")
rptObj.ui.fields.integer(label="test", value="Test 2", placeholder="Number", icon="fas fa-sort-numeric-up-alt", helper="Youpi")
p = rptObj.ui.fields.password(label="test", value="Test 2", placeholder="password", icon="fas fa-unlock-alt")
rptObj.ui.fields.range(54, min=20, label="test", icon="fas fa-unlock-alt")

rptObj.ui.fields.checkbox(True, label="Check")
rptObj.ui.fields.radio(True, label="Check", group_name="test")
rptObj.ui.fields.radio(False, label="Check", group_name="test")
rptObj.ui.fields.radio(False, label="Check", group_name="test")

rptObj.ui.fields.textarea("Test", label="Check")

rptObj.ui.inputs.search()

ch = rptObj.ui.inputs.checkbox(False)
rptObj.ui.inputs.radio(False, label="checkbox")
s = rptObj.ui.fields.select(["A", "B"], label="Select Test")
b = rptObj.ui.buttons.radio(["A", "B", "C"], checked="B")
b.click([
  s.dom.highlight(css_attrs={"background": "red"}),
  #ch.dom.highlight(),
  #sw.dom.highlight(),
])

i.input.focus(rptObj.js.console.log("ok"), options={"reset": True})
p.input.focus(rptObj.js.console.log("ok"), options={"reset": True})


# ----------------
# Component Inputs
rptObj.ui.fields.today("2019-11-18", label="timestamp", color="red", helper="This is the report timestamp")
rptObj.ui.fields.now(label="timestamp", color="red", helper="This is the report timestamp")
rptObj.ui.fields.cob(label="Date").selectable(["2019-09-01", "2019-09-06"])

#-------------------

#
input = rptObj.ui.inputs.checkbox(True)
input.set_attrs(name="type", value="checkbox")
input.tooltip("Test")

# input.click(
#   [rptObj.js.alert(input.dom.content)]
# )

rptObj.ui.inputs.input("RRRRRRRRR")

input = rptObj.ui.input()
#input.quantity()
input.enter(rptObj.js.console.log(input.dom.val))

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_input"))
