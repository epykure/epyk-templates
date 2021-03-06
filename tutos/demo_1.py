"""

http://pypl.github.io/PYPL/All.js?t=axbAll7888Allbxa

"""

from epyk.core.css.themes import ThemeBlue
from epyk.core.js import std
from epyk_studio.core.Page import Report


page = Report()
page.headers.dev() # Change the Epyk logo
page.theme = ThemeBlue.BlueGrey()

page.js.customFile("FR.js", r"http://pypl.github.io/PYPL")

title = page.ui.title("PYPL PopularitY of Programming Language")
items = page.ui.inputs.autocomplete(placeholder="select a language and press enter", options={"select": True})

cols_keys = page.ui.lists.drop(htmlCode="cols_agg_keys")
cols_keys.style.css.min_height = 20
cols_keys.items_style(style="bullets")
cols_keys.drop()

items.enter([cols_keys.dom.add(items.dom.content), items.dom.empty()])

button = page.ui.buttons.colored("Display")
button.style.css.margin_top = 5

line = page.ui.charts.chartJs.line(x_axis="Date")
line.options.scales.x_axes().type = "time"
line.options.elements.point.radius = 0
line.options.scales.x_axes().distribution = 'linear'

box = page.studio.containers.box()
box.extend([title, items, cols_keys, button, line])
box.style.standard()

button.click([
  std.var("graphData").fromArrayToRecord().setVar("records"),
  line.build(std.var("records"), options={"y_columns": cols_keys.dom.content, "x_axis": "Date"})
])

page.body.onReady([items.js.source(std.var("graphData")[0])])
