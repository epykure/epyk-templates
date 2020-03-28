
import config
from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()

#input = rptObj.ui.inputs.d_range(3)
#text_area = rptObj.ui.inputs.textarea("This is a textarea")
#date = rptObj.ui.dates.now(label="date")
# rptObj.ui.texts.up_down({'previous': 100880, 'value': 240985})
# rptObj.ui.texts.up_down({'previous': 1000880, 'value': 240985})
#
# rptObj.ui.rich.textbubble({"value": 23, "title": "Title"}, helper="This is a helper")

#rptObj.ui.rich.blocktext({"text": 'This is a brand new python framework', "title": 'New Python Web Framework',
#                            "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})

# light = rptObj.ui.rich.light(True, label="label", tooltip="Tooltip", helper="Helper")
# light.colors(red='yellow', green="blue")
#
# rptObj.ui.texts.formula("$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$", helper="This is a formula")

#rptObj.ui.rich.vignet({'title': 'Python', 'number': 100, 'text': 'Content', 'color': 'green', 'url':
#                           'https://www.python.org/', 'icon': 'fab fa-python', 'tooltip': 'Python Fondation',
#                           'urlTitle': 'WebSite'})

# rptObj.ui.rich.textborder({"title": "New Python Framework", 'value': "A new Python Web Framework", 'color': 'green',
#                              'icon': 'fab fa-python', 'colorTitle': 'darkgreen'})
#

# rptObj.ui.rich.prism("print('test')")

# edit = rptObj.ui.icons.edit()
# edit.on('click', rptObj.js.console.log('test'))
#
# rptObj.ui.icons.clock().css({"color": 'blue'})
# rptObj.ui.icons.edit().color("red")

# rptObj.ui.buttons.check(label="Label")

#env = rptObj.ui.icons.awesome(
#  rptObj.ui.icons.get.ICON_ENVELOPE, text=2)

#env.icon_css({"background": 'MistyRose', 'font-size': '20px'})
#env.span.style.addCls("fa-layers-counter")

# stars = rptObj.ui.rich.stars(3, label="test", helper="This is a helper")
# stars.click()
#
# rptObj.ui.info("Test", options={"css": {"color": 'red'}})
#
# rptObj.ui.loading("Loading component", options={"fixed": True})

#rptObj.ui.links.external("google", "https://fontawesome.com/how-to-use/on-the-web/styling/layering")
# contents = rptObj.ui.contents()
#
# rptObj.ui.title("title", contents=contents)
# rptObj.ui.title("title", level=2, contents=contents)
# rptObj.ui.title("title", contents=contents)
#
# number = rptObj.ui.rich.number(500, "Test", height=(150, 'px'))
# number.add_label("This is a first **label** to be checked", position="after", css={"margin": 0})
# number.label.add_options({"css": {"color": 'red'}})
# number.span.add_icon(rptObj.ui.icons.get.ICON_ENVELOPE)
#
# data_link = rptObj.ui.links.data("link", "test#data")
#
# number_2 = rptObj.ui.rich.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
# number_3 = rptObj.ui.rich.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
# number_4 = rptObj.ui.rich.number(500, "Test 2 ", options={"url": "http://www.google.fr"})

# label = rptObj.ui.texts.label("T **e** st").css({"float": 'none'})
# label.add_checkbox(True)
# label.add_title("THis is a title")

# rptObj.ui.layouts.div(
#   rptObj.ui.inputs.checkbox(True, label="Text", group_name="test", htmlCode="my_radio")).css({"border": '1px solid black'})
#
# rptObj.ui.inputs.radio(False, label="Text", group_name="test")
# rptObj.ui.inputs.radio(False, label="Text", group_name="test")
#
#
# rptObj.itemFromCode("my_radio").click([
#   rptObj.js.alert("")
# ])

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
# rptObj.itemFromCode("test").click([
#   rptObj.itemFromCode("content").dom.hide().r,
#   rptObj.itemFromCode("content2").dom.show().r
# ])


# rptObj.ui.sliders.progressbar(40)
# # rptObj.ui.slider(recordSet=[1, 2, 3, 4, 5, 6, 7])
# rptObj.ui.options_bar([
#   {"icon": "fab fa-accusoft"},
#   {"icon": "fab fa-accusoft"},
# ]).draggable()
#
# rptObj.ui.icons.signin("RRR")

# rptObj.ui.layouts.dialogs()
#rptObj.ui.images.animated()
#
# from epyk.core.html import Defaults
#
# Defaults.SERVER_PATH = r"C:\Pictures"
# rptObj.ui.images.animated("philo.PNG")

# s = rptObj.ui.select(["A", "B", "C"], label="label", selected="C", multiple=True,
#                      options={"title": "ttle", 'showTick': True, 'maxOptions': 2})
# s.selected = "B"
# s.change(rptObj.js.console.log(s.dom.val))
# rptObj.ui.buttons.zipfile("This is the data", "filename.txt")


#l = rptObj.ui.lists.categories(["AWW", "B"], categories=["youpi"])
#l.add_list(["D", "E"], category="Test")
#l[0].css({"color": "red"})

#l.set_items_format('fab fa-python', 'python', css_attrs={"color": 'red'})

data = [{"value": 'test', '_children': [
  {"label": 'child 1', 'color': 'red', 'value': 'red'},
  {"label": 'child 1', 'color': 'red', 'value': 'blue'}
]},{
   "value": 'prog', '_children': [
    {'value': 'python'},
  ]
         }]
# rptObj.ui.lists.dropdown(data)
#
# l = rptObj.ui.lists.list(["A", "B"])
#
# b = rptObj.ui.button("Click me")
#
# b.click([
#   b.build("RRRR"),
#   l.refresh(),
#   b.build("Test"),
# ])

# rptObj.ui.workflow([
#   {"value": 'test 1', "status": 'success', 'label': 'test'},
#   {"value": 'test 1', "status": 'success'},
#   {"value": 'test 1', "status": 'success'},
#   {"value": 'test 2', "status": 'error', 'label': 'X'},
#   {"value": 'test 3', "status": 'pending'},
#   {"value": 'test 3'},
#   {"value": 'test 3'},
# ])

c1 = rptObj.ui.images.badge(3, icon="far fa-bell", url="test")
c1.style.display = None

rptObj.ui.layouts.div([c1], align='right')

rptObj.ui.button("display").click(c1.dom.toggle())

rptObj.ui.layouts.hr()

rptObj.ui.texts.number(28, title="Total RFQs", color="green")
rptObj.ui.texts.number(9, title="Working", color="orange")
rptObj.ui.texts.number(4, title="Done", color="green")
rptObj.ui.texts.number(15, title="Missed", color="red")

rptObj.ui.charts.sparkline("bar", [1, 2, 3], title="Top Clients (#)",  options={"barWidth": 20})

rptObj.ui.layouts.hr()

rptObj.ui.row([
  rptObj.ui.title("test"),
  #rptObj.ui.tables.tabulators
])

s = rptObj.ui.select(["A", "B"], label="test")
s.selected = "B"
s.change([rptObj.js.console.log(s.dom.val)])

w = rptObj.ui.workflow([
  {"value": 'test 1', "status": 'success', 'label': 'test'},
  {"value": 'test 1', "status": 'success'},
  {"value": 'test 1', "status": 'success'},
  {"value": 'test 1', "status": 'success'},
  {"value": 'test 1', "status": 'pending'},
  {"value": 'test 1'},
  {"value": 'test 1'},
  {"value": 'test 1'},
])

rptObj.ui.button("worklow").click([
  w.dom.set_complete(5)
])

rptObj.ui.rich.countdown("2020-09-24")
rptObj.ui.rich.update("Last update: ")

t = rptObj.ui.title("RFQ Details", level=4).css({"float": 'left'})

rptObj.ui.layouts.div([t, w])

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
#sw = rptObj.ui.buttons.switch()
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


#rptObj.ui.layouts.iframe("http://www.google.com")

# menu = rptObj.ui.layouts.icons()
# menu.add_icon("fab fa-accusoft")
# menu.add_icon("fab fa-accusoft")
#
# menu.icon.click([menu.icon.dom.css({"color": 'red'})])

# data = [
#   {"value": 23, "name": 'test'},
#   {"value": 45, "name": 'test2'}]
# rptObj.ui.charts.skillbars(data, y_column="value", x_axis="name")


# rptObj.itemFromCode("test3").click([
#   rptObj.itemFromCode("content2").dom.hide().r,
#   rptObj.itemFromCode("content").dom.show().r
# ])

#rptObj.ui.lists.dropdown([])

# ----------------
# Component Inputs
#rptObj.ui.dates.today("2019-11-18", label="timestamp", color="red", helper="This is the report timestamp")
#rptObj.ui.dates.now(label="timestamp", color="red", helper="This is the report timestamp")
#rptObj.ui.dates.cob(label="Date").selectable(["2019-09-01", "2019-09-06"])

#rptObj.ui.dates.countdown("2019-11-24")
#rptObj.ui.dates.update("test")
#-------------------


# tab = rptObj.ui.layouts.pills()
# tab.add_panel("test", rptObj.ui.div("Test Content"))
# tab.add_panel("test 2", rptObj.ui.div("Test Content 2"))
#
#
# tab2 = rptObj.ui.layouts.tabs()
# tab2.add_panel("test", rptObj.ui.div("Test Content"))
# tab2.add_panel("test 2", rptObj.ui.layouts.col([
#   rptObj.ui.div("Test Content 3")]))
#
#
# fixed = rptObj.ui.layouts.slide([], title="This is a title")
# fixed += rptObj.ui.title("Sub title")

#fixed.title.click([
#  rptObj.js.getElementsByName("panel_%s" % fixed.htmlId).first.toggle()
#])


# number = rptObj.ui.rich.number(500, "Test", height=(150, 'px'))
# number_2 = rptObj.ui.rich.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
# fixed += rptObj.ui.layouts.panelsplit(left=number, right=number_2)
#
# radio = rptObj.ui.radio(["A", "B", "C"], checked="B")
# radio + "G"
# radio.set_checked("G")
# radio.set_disable("B")

#tab.tab("test 2").css({"background": 'red'})

# button = rptObj.ui.button("test")
# button.click([
#   #rptObj.js.alert(rptObj.js.getElementsByName(tab.panels_name).length),
#   rptObj.js.getElementsByName(tab.panels_name).all([
#     rptObj.js.data.all.element.hide(),
#     tab.panel("test 2").dom.show(),
#   ])
# ])

# #rptObj.ui.inputs.radio(False)

# label.checkbox.click([
#   rptObj.js.alert("Test")
# ])

#
# input = rptObj.ui.inputs.checkbox(True)
# input.set_attrs(name="type", value="checkbox")
# # input.tooltip("Test")
#
# input.click(
#   [rptObj.js.alert(input.dom.content)]
# )

#rptObj.ui.inputs.input("RRRRRRRRR")

# list = rptObj.ui.lists.styles()
# list.add_list("test", ["Test", "test 2"])
# list.add_list("test2", ["Test", "test 2"])

#list.add_label("This is a label", css=False)
#list.add_title("This is a title", css=False)
# list.set_items(data=["A", "B"])
#list.set_items(css_attrs={"border": '1px solid black'})
#list.items[0].add_title("title")

#div = rptObj.ui.layouts.panelsplit(left=number, right=number_2, resizable=True)
#div = rptObj.ui.layouts.tabs([number, number_3, number_2, number_4])
#
# rptObj.ui.tags.comment("This is an HTML comment")
# abbr = rptObj.ui.tags.bdi("abbr")
# abbr.click(rptObj.js.alert("test"))
# abbr.css({'cursor': 'pointer', 'border': '1px solid black'})

#iframe = rptObj.ui.layouts.iframe(r"https://www.google.com/search?client=avast&q=gopro")
#div = rptObj.ui.layouts.fixed([number, number_2])

#div += number_2

# rptObj.ui.rich.blocktext({"text": 'This is a brand new python framework', "title": 'New Python Web Framework',
#                           "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})
#
# number.span.tooltip("TEST")
#
# input = rptObj.ui.input()
#
# b = rptObj.ui.button("test")
# b.click([
#   number.span.build("ok"),
#   data_link.build({"text": 'new link Name', 'data': "new content"}),
#   number_2.span.build({"text": input.dom.content}),
  #iframe.build("https://replaytvstreaming.com/spectacle/5344-jo.html")
# ])
#env.span.set_attrs(name="href", value="google")
#input.quantity()
#input.enter(rptObj.js.console.log(input.dom.val))

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_input"))
