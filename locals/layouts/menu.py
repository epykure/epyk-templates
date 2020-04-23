
import config

from epyk.core.Page import Report
from epyk.core.css.themes import ThemeDark

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

#rptObj.theme = ThemeDark.Grey()
record = [{"text": "Lin 1", 'url': 'report_list.html'}, {"text": "Link 2"}]
rptObj.ui.navigation.pin("anchor", tooltip="test", bottom=20)
#rptObj.ui.text("test").css({"display": 'inline-block'})
#rptObj.ui.text(rptObj.symbols.shapes.BLACK_RIGHT_POINTING_TRIANGLE).css({"display": 'inline-block'})
#rptObj.ui.text("test").css({"display": 'inline-block'})


mb = rptObj.ui.menus.button("Value", rptObj.ui.list(["value 1", "value 2"]))
mb.item.click([rptObj.js.alert(mb.item.dom.content)])

rptObj.ui.images.badge(12, icon="far fa-bell", options={"badge_position": 'right'})

tb = rptObj.ui.menus.toolbar(["fas fa-paint-brush", "fas fa-code"])
tb[1].link.val = 4589
tb[1].tooltip("This is a tooltip")
tb[0].style.css.color = 'red'

ds = rptObj.ui.menus.divisor(["Link 1", 'Link 2', 'Link 3'])
ds.texts[0].click([
  rptObj.js.alert(ds.texts[0].dom.content)
])

bs = rptObj.ui.menus.buttons(["Button", "Button 2", "Button 3"])
bs[2].click([
  rptObj.js.alert(bs[2].dom.content)
])

# rptObj.ui.div(
#   [rptObj.ui.text("test 1"),
#    [rptObj.ui.text("test2", width=None), rptObj.ui.text("test3", width=None)]]
# )


record = [
  {"value": 'A', 'title': 'Title', 'children': [
    "item 1",
    "item 2",
    "item 3",
  ]},
  {"value": 'B', 'title': 'Title 2', 'children': [
    "item 1",
    "item 2",
    "item 3",
  ]},
  {"value": 'C', 'title': 'Title 3', 'children': [
    [
    "item C",
    "item 2",
    "item 3"],
    [
      "item 424",
    ]
  ]},
  {"value": 'D', 'title': 'Title 4', 'children': [
    "item C",
    "item 2",
    "item 3",
  ]},
]

#top = rptObj.ui.menus.menu(record,
#      options={"li_css": {"color": 'white', "padding": '5px 16px', "display": 'inline-block'},
#        "li_class": ["CssDivOnHoverBackgroundLight", "CssTextNotSelectable"],
#      })
#      })

div = rptObj.ui.div(width=(100, "px"))
div.style.css_padding_left = "5px"
div.style.css_margin_top = 5

for i in range(5):
  item = rptObj.ui.div("Menu %s" % i).css({"padding": "1px 10px", "margin": "2px 0", "color": rptObj.theme.colors[7],
                                           "border-left": "1px solid %s" % rptObj.theme.greys[0]})
  item.attr["name"] = div.htmlId
  item.style.add_classes.div.background_hover()
  item.click([
    item.dom.by_name.css({"border-left": "1px solid %s" % rptObj.theme.greys[0], "color": rptObj.theme.colors[7]}).r,
    item.dom.css({"border-left": "1px solid %s" % rptObj.theme.success[1], "color": rptObj.theme.colors[-1]})
  ])
  item.inReport = False
  div + item


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
