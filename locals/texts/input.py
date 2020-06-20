
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

input = page.ui.inputs.d_range(3)
text_area = page.ui.inputs.textarea("This is a textarea")


contents = page.ui.contents()

# page.ui.title("title", level=2, contents=contents)
# page.ui.title("title", contents=contents)
#
# number = page.ui.rich.number(500, "Test", height=(150, 'px'))
# number.add_label("This is a first **label** to be checked", position="after", css={"margin": 0})
# number.label.add_options({"css": {"color": 'red'}})
# number.span.add_icon(page.ui.icons.get.ICON_ENVELOPE)
#
# page.ui.layouts.div([
#   page.ui.div("Test", width=("100", "px"), htmlCode="test").css({"border": '1px solid black', 'display': 'inline-block'}),
#   page.ui.div("Test2", width=("100", "px")).css({"border": '1px solid black', 'display': 'inline-block'}),
#   page.ui.div("Test3", width=("100", "px"), htmlCode="test3").css({"border": '1px solid black', 'display': 'inline-block'}),
#   page.ui.div("Test4", width=("100", "px")).css({"border": '1px solid black', 'display': 'inline-block'}),
#   page.ui.div([
#     page.ui.rich.number(100, "Number"),
#     page.ui.rich.prism("print('test')"),
#   ], htmlCode="content").css({'display': 'none'}),
#   page.ui.div("Test4", htmlCode="content2").css({'display': 'none'}),
# ], width=("auto", ""))
#

# page.ui.options_bar([
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


# w = page.ui.workflow([
#   {"value": 'test 1', "status": 'success', 'label': 'test'},
#   {"value": 'test 1', "status": 'success'},
#   {"value": 'test 1', "status": 'success'},
#   {"value": 'test 1', "status": 'success'},
#   {"value": 'test 1', "status": 'pending'},
#   {"value": 'test 1'},
#   {"value": 'test 1'},
#   {"value": 'test 1'},
# ])

# page.ui.button("worklow").click([
#   w.dom.set_complete(5)
# ])

# t = page.ui.inputs.textarea("Test", placeholder='This is a placeholer')
# t.selectable()
# t.options.rows = 10

page.ui.row([
  page.ui.title("test"),
  page.ui.col([
    page.ui.rich.light("red", label="test", tooltip="Test"),
    page.ui.rich.light(True, label="test"),
    page.ui.rich.light(False, label="test"),
    page.ui.fields.now(label="test")
  ])
])

input = page.ui.input()
input.options.css({"color": 'red'})
input.options.toFixed(4)

page.ui.button("Build Input").click([
  # For the color to orange to show the button has been clicked
  input.build("1234.456789")
])

page.ui.fields.input(label="Label Input")
page.ui.fields.now(label="test")
page.ui.fields.cob(label="test")

i = page.ui.fields.static(label="test", value="Test 2", placeholder="Read only", helper="RRRR")
page.ui.fields.integer(label="test", value="Test 2", placeholder="Number", icon="fas fa-sort-numeric-up-alt", helper="Youpi")
p = page.ui.fields.password(label="test", value="Test 2", placeholder="password", icon="fas fa-unlock-alt")
page.ui.fields.range(54, min=20, label="Range 1", icon="fas fa-unlock-alt").tooltip("With an output")
page.ui.fields.range(54, min=20, label="Range 2", icon="fas fa-unlock-alt", options={"output": False})

page.ui.fields.checkbox(True, label="Check")
page.ui.fields.radio(True, label="Check", group_name="test")
page.ui.fields.radio(False, label="Check", group_name="test")
page.ui.fields.radio(False, label="Check", group_name="test")

page.ui.fields.textarea("Test", label="Check")

page.ui.inputs.search()

ch = page.ui.inputs.checkbox(False)
page.ui.inputs.radio(False, label="checkbox")
s = page.ui.fields.select(["A", "B"], label="Select Test")
b = page.ui.buttons.radio(["A", "B", "C"], checked="B")
b.click([
  s.dom.highlight(css_attrs={"background": "red"}),
  #ch.dom.highlight(),
  #sw.dom.highlight(),
])

i.input.focus(page.js.console.log("ok"), options={"reset": True})
p.input.focus(page.js.console.log("ok"), options={"reset": True})


# ----------------
# Component Inputs
page.ui.fields.today(label="timestamp", color="red", helper="This is the report timestamp")
page.ui.fields.now(label="timestamp", helper="This is the report timestamp")
page.ui.fields.cob(label="Date")

#-------------------

#
input = page.ui.inputs.checkbox(True)
input.set_attrs(name="type", value="checkbox")
input.tooltip("Test")

# input.click(
#   [page.js.alert(input.dom.content)]
# )

page.ui.inputs.input("RRRRRRRRR")

input = page.ui.input()

input.enter(page.js.console.log(input.dom.val))

