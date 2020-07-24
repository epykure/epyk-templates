
from epyk.core.Page import Report
from epyk.tests import data_urls
from websites.material import blablacar_data

import random

page = Report()


data_rest = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)


page.body.style.globals.size = 18

slides = page.ui.vignets.slides(start=0)

slides.style.css.display = "block"
contents = page.ui.contents("Contente")

slides.add_slide("Epyk - A web Studio library", [
  page.ui.title('''
A centralise library for linking   
'''),
  page.ui.img("epyklogo_whole_big.png?raw=true", path="https://github.com/epykure/epyk-ui/blob/master/epyk/static/images/", width=(300, 'px'))
])

slides.add_slide("Epyk - Architecture", [

  page.ui.img("architecture.PNG?raw=true", path="https://github.com/epykure/epyk-ui/blob/master/epyk/static/images", width=(500, 'px'))
])

# Using standard Javascript Libraries
slides.add_slide("Epyk - Analytics", [
  page.ui.row([
    page.ui.charts.chartJs.bar(data_rest, y_columns=['AAPL.Open'], x_axis="Date", height=(200, 'px')),
    page.ui.charts.chartJs.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date", height=(200, 'px'))
  ])
])

# -------------------------
# Of course using the underlying Dash library
data_rest = page.py.requests.csv(data_urls.PLOTLY_3D)

slides.add_slide("Epyk - Plotly", [
  page.ui._3d.plotly.ribbon(data_rest, y_columns=["y1"], x_axis='x1', z_axis="z1", width=(400, 'px'))
])

# -------------------------
# Ceinralise your team work for free
data = [
    {"id": 0, "group": 0, "content": 'item 0', "start": "2020-06-29", 'type': 'point'},
    {"id": 0, "group": 0, "content": 'item 0', "start": "2020-06-17", "end": "2020-06-21"},
    {"id": 1, "group": 0, "content": 'item 1', "start": "2020-06-10", "end": "2020-06-20", 'type': 'background'},
    {"id": 2, "group": 1, "content": 'item 2', "start": "2020-06-16", "end": "2020-06-24"},
    {"id": 3, "group": 1, "content": 'item 3', "start": "2020-06-23", "end": "2020-06-24", 'type': 'box'},
    {"id": 4, "group": 1, "content": 'item 4', "start": "2020-06-24", "end": "2020-06-26"},
    {"id": 5, "group": 2, "content": 'item 5', "start": "2020-06-24", "end": "2020-06-27"}
  ]

groups = [
  {"id": 1, 'content': 'test 1'},
  {"id": 2, 'content': 'test 2'},
  {"id": 3, 'content': 'test 3'},
  {"id": 0, 'content': 'test 0'},
]

timeline2 = page.ui.charts.vis.timeline(data, content="content", start='start', end="end", type="type", group="group", options={"type": 'box'})
timeline2.options.stack = True
timeline2.setGroups(groups)

rows = []
#rows.append(page.ui.row(["Category", "", "Timelines", "Progression", "", "", "", "Status", "Activity", "Files"]))
rows.append(["Category", "", "Timelines", "Progression", "", "", "", "Status", "Activity", "Files"])

for i in range(10):
  rows.append([
    page.ui.div("This is a text").css({"border-left": '1px solid %s' % page.theme.success[1], 'padding-left': '10px',
                                         'background': page.theme.success[0]}),
    page.ui.timelines.view("2020-01-05", "2020-%s-%s" % (random.randint(1, 12), random.randint(1, 25))),
    page.ui.sliders.progress(random.randint(1, 100)),
    page.ui.charts.sparkline("line", [random.randint(1, 25) for i in range(10)], width=("40", 'px')),
  ])

slides.add_slide("Epyk - Time Tracker (Agile Teams)", [
  timeline2,
  page.ui.grid(rows)
])


# -------------------------
# But also a real web studio

row = []
for k, v in blablacar_data.CATEGORIES.items():
  row.append(page.ui.vignets.vignet(title=k, content=v))

button_style = {"border-radius": '20px', 'background-color': 'rgb(0, 175, 245)', 'color': 'white', 'padding': '8px 25px', 'font-size': '18px'}
button_inv_style = {"border-radius": '20px', 'background-color': 'white', 'color': 'rgb(0, 175, 245)', 'padding': '8px 25px', 'font-size': '18px'}
title_style = {"width": '90%', 'margin': 'auto', 'font-weight': 800, 'line-height': '1.06', 'font-size': '30px', 'color': 'rgb(5, 71, 82)', 'padding': '24px 0px'}

button = page.ui.button(blablacar_data.BUTTON_OFFER_RIDW, align="center")
button.style.css.margin_top = 10
button.css(button_style)

content = page.ui.col([page.ui.text(blablacar_data.SLOGAN, width=(100, "%")), button])
content.style.css.padding = 0


slides.add_slide("Epyk - Web Studio", [
  page.ui.title("Car Compagny").css({"margin-top": '130px'}),
  page.ui.vignets.image(blablacar_data.VIGNET_2['title'], content=content, image=blablacar_data.VIGNET_2['image']),
  page.ui.titles.title(blablacar_data.TITLE_1).css(title_style),
  page.ui.row(row, align="center", position="top")
])

page.body.onReady([
  contents.build([
    {"anchor": '#test', 'level': 1, 'text': 'Overview'}
  ])
])