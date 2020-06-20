

from epyk.core.Page import Report
from epyk.core.html import Defaults
from epyk.core.css.themes import ThemeDark


Defaults.TEXTS_SPAN_WIDTH = None

# Create a basic report object
page = Report()
page.headers.dev()


page.ui.titles.head("Test")
page.ui.titles.headline("Test")
page.ui.titles.rubric("Test")
page.ui.titles.underline("Test")
page.ui.titles.caption("Test")
page.ui.text("Test")

input = page.ui.input()

i = page.ui.lists.badges([
  {"text": 'text', 'icon': 'fas fa-times', 'checked': True, 'value': 8},
  {"text": 'text', 'icon': 'fas fa-times', 'checked': True, 'value': 5},
], options={"badge": {"background": 'green'}})
i.click([
  page.js.console.log(i.dom.content),
])

c = page.ui.lists.items([
  {"text": 'value 1', 'icon': 'fas fa-times', 'checked': True, 'value': 8000},
  {"text": 'value 1', 'icon': 'fas fa-times', 'checked': True, 'value': 50000},
], options={"style": {"background": 'green'}})

page.jsImports.add("accounting")
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

page.ui.button("Get").click([
  page.js.console.log(i.dom.content),
])
# input = page.ui.input()
# tags = page.ui.lists.chips(["ok", 'Test'])
#
# page.ui.button("Click").click([
#   page.js.console.log( tags.dom.content )
#   #tags.dom.add("Youpi")
# ])
#
#
# page.ui.button("Add").click([
#   tags.dom.add(input.dom.content)
# ])
#
# page.ui.button("Toggle Display").click([
#   tags.dom.toggle(),
#   #tags.dom.add("Youpi")
# ])
#
#
# page.ui.button("Remove").click([
#   tags.dom.remove(input.dom.content),
#   #tags.dom.add("Youpi")
# ])


#page.theme = ThemeDark.Dark()

# Console component
# c = page.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})
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
# page.ui.lists.numbers(["A", "B"])
# page.ui.lists.alpha(["A", "B"])
#
# t = page.ui.lists.dropdown(data)
# t.options.expanded = False
# #t.level(1)
#
#
# page.ui.lists.tags(["ok", 'Test'])


#
#
# page.js.addOnReady([
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

# page.ui.button("test").click([
#   page.js.window.toggleInterval(page.js.console.log('ok'), 'test', 400),
# ])
#
#
# s = page.ui.select(["A", "B", "C"], label="label", selected="C", multiple=True,
#                       options={"title": "ttle", 'showTick': True, 'maxOptions': 2})
# s.selected = "B"
# s.change(c.write(s.dom.content))

#
# l2 = page.ui.list(range(10))
#
# #
# l3 = page.ui.list(range(10)).css({"color": "red"})
#

#
# l2.add_item(l3)[-1].val.css({"margin": "2px 10px"})
#
# #l2[-1].set_html_content(page.ui.texts.span(l2[-1].val))
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
# l = page.ui.lists.categories(["AWW", "B"])
# l.add_list(["D", "E"], category="Test")
# for i in l:
#   for u in i:
#     u.no_decoration
#
#
# data = [{"label": "python", "value": False}, {"label": "Java", "value": 5}]
# checks = page.ui.lists.checklist(data)
# #
# page.ui.button("Test").click([
#   checks.items[1].dom.toggle()
# ])
#
#
# bs = page.ui.lists.buttons(["Button", "Button 2", "Button 3"])
# bs = page.ui.buttons.buttons(["Button", "Button 2", "Button 3"])
# print(bs[2].content)
# bs[2].click([
#   page.js.alert(bs[2].dom.content)
# ])
#

