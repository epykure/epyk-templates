
import config

from epyk.core.Page import Report
from epyk.core.html import Defaults
from epyk.core.css.themes import ThemeDark

Defaults.TEXTS_SPAN_WIDTH = None

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo


rptObj.ui.titles.head("Test")
rptObj.ui.titles.headline("Test")
rptObj.ui.titles.rubric("Test")
rptObj.ui.titles.underline("Test")
rptObj.ui.titles.caption("Test")
rptObj.ui.text("Test")

input = rptObj.ui.input()

i = rptObj.ui.lists.badges([
  {"text": 'text', 'icon': 'fas fa-times', 'checked': True, 'value': 8},
  {"text": 'text', 'icon': 'fas fa-times', 'checked': True, 'value': 5},
], options={"badge": {"background": 'green'}})
i.click([
  rptObj.js.console.log(i.dom.content),
])

c = rptObj.ui.lists.items([
  {"text": 'value 1', 'icon': 'fas fa-times', 'checked': True, 'value': 8000},
  {"text": 'value 1', 'icon': 'fas fa-times', 'checked': True, 'value': 50000},
], options={"style": {"background": 'green'}})

rptObj.jsImports.add("accounting")
c.add_type('number', '''
var item = document.createElement("DIV");
item.setAttribute('name', 'value'); item.setAttribute('data-valid', true);
if(options.click != null){ 
  item.style.cursor = 'pointer'; item.onclick = function(event){var value = this.innerHTML; options.click(event, value)}};
var text = document.createElement("DIV"); text.innerHTML = data.text +":&nbsp;";
text.style.display = "inline-block";
var value = document.createElement("DIV"); value.innerHTML = accounting.formatNumber(data.value);
value.style.display = "inline-block";
item.appendChild(text); item.appendChild(value);
''')

input.enter([
  i.dom.add({"text": input.dom.content, "checked": True}),
])

rptObj.ui.button("Get").click([
  rptObj.js.console.log(i.dom.content),
])
# input = rptObj.ui.input()
# tags = rptObj.ui.lists.chips(["ok", 'Test'])
#
# rptObj.ui.button("Click").click([
#   rptObj.js.console.log( tags.dom.content )
#   #tags.dom.add("Youpi")
# ])
#
#
# rptObj.ui.button("Add").click([
#   tags.dom.add(input.dom.content)
# ])
#
# rptObj.ui.button("Toggle Display").click([
#   tags.dom.toggle(),
#   #tags.dom.add("Youpi")
# ])
#
#
# rptObj.ui.button("Remove").click([
#   tags.dom.remove(input.dom.content),
#   #tags.dom.add("Youpi")
# ])


#rptObj.theme = ThemeDark.Dark()

# Console component
# c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})
#
# data = [{"label": 'test', 'items': [
#   {"label": 'child 1', 'color': 'red'},
#   {"label": 'child 2', 'color': 'green', 'items': [
#       {"label": 'sub child 1', 'color': 'red'},
#   ]},
#   {"label": 'child 3', 'color': 'red'},
#
# ]}]
#
# rptObj.ui.lists.numbers(["A", "B"])
# rptObj.ui.lists.alpha(["A", "B"])
#
# t = rptObj.ui.lists.dropdown(data)
# t.options.expanded = False
# #t.level(1)
#
#
# rptObj.ui.lists.tags(["ok", 'Test'])


#
#
# rptObj.js.addOnReady([
#   s.input.dom.ajaxSelectPicker({"ajax": {
#     #"beforeSend": "function(){console.log(%s)}()" % s.input.dom.content,
#     #"url": 'function(element){return "https://jsonplaceholder.typicode.com/posts/"}(this)' % s.input.dom.search,
#     'url': 'function(){return "https://jsonplaceholder.typicode.com/posts/" + this.plugin.query}',
#     "type": "get", "dataType": "json", "data": "",
#     #"data": {"q": "{{{q}}}"}
#     },
#         'preserveSelected': False, 'preprocessData':
#         'function(data) {return [{text: "C", value: "C"}, {text: "D", value: "D"}]}', "locale": {
#     "emptyTitle": "Select and Begin Typing"}})
# ])

# rptObj.ui.button("test").click([
#   rptObj.js.window.toggleInterval(rptObj.js.console.log('ok'), 'test', 400),
# ])
#
#
# s = rptObj.ui.select(["A", "B", "C"], label="label", selected="C", multiple=True,
#                       options={"title": "ttle", 'showTick': True, 'maxOptions': 2})
# s.selected = "B"
# s.change(c.write(s.dom.content))

#
# l2 = rptObj.ui.list(range(10))
#
# #
# l3 = rptObj.ui.list(range(10)).css({"color": "red"})
#

#
# l2.add_item(l3)[-1].val.css({"margin": "2px 10px"})
#
# #l2[-1].set_html_content(rptObj.ui.texts.span(l2[-1].val))
# l2[-1].add_label("test")
# l2[-1].add_icon("fas fa-folder")

#
# l2[-1].label.tooltip("test")
# l2[-1].icon.click([
#   l2[-1].val.dom.toggle(),
#   l2[-1].icon.dom.switchClass("fa-folder", "fa-folder-open")
# ])
#
# l2.add_item(14)
#
# l.add_item(l2)[-1].val.css({"margin": "0px 10px"})
#
# #l2.set_items_format(icon="fas fa-folder")
# #l3.set_items_format(icon="fas fa-archive")
# #l.set_items_format(icon="fas fa-archive")
#
#
# l = rptObj.ui.lists.categories(["AWW", "B"])
# l.add_list(["D", "E"], category="Test")
# for i in l:
#   for u in i:
#     u.no_decoration
#
#
# data = [{"label": "python", "value": False}, {"label": "Java", "value": 5}]
# checks = rptObj.ui.lists.checklist(data)
# #
# rptObj.ui.button("Test").click([
#   checks.items[1].dom.toggle()
# ])
#
#
# bs = rptObj.ui.lists.buttons(["Button", "Button 2", "Button 3"])
# bs = rptObj.ui.buttons.buttons(["Button", "Button 2", "Button 3"])
# print(bs[2].content)
# bs[2].click([
#   rptObj.js.alert(bs[2].dom.content)
# ])
#

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
