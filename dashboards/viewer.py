
from epyk.core.Page import Report
from epyk.core.css.themes.ThemeDark import Grey

from epyk.core.data import events
from epyk.core.data import datamap

from epyk.web import angular

#
# Create a basic report object
page = Report()
page.headers.dev()
page.theme = Grey()

#
page.ui.navigation.shortcut([
  page.ui.layouts.hr(),
  page.ui.titles.title("From to"),
  page.ui.date(width=(100, "px"), htmlCode='date'),
  page.ui.layouts.hr(),
  page.ui.titles.title("Desks"),
  page.ui.button("Data 1", htmlCode="button", icon="fab fa-angular"),
  page.ui.button("Data 2", icon="fab fa-angular"),

  #page.ui.icons.awesome("fab fa-angular").css({"right": '10px', 'position': 'absolute'}),
  page.ui.row([
    page.ui.icons.awesome("far fa-file-pdf"),
    page.ui.icons.awesome("fas fa-at"),
  ]).css({"bottom": '10px', 'position': 'absolute', 'display': 'block'})
], size=(100, 'px'), options={"position": 'left'})

page.body.style.css.margin_left = 110

content = ""
#with open(r".\interactives\data\md_file.md") as f:
#  content = f.read()

page.ui.text(content, htmlCode="text", options={"markdown": True})

footer = page.ui.navigation.footer('''
This is a disclaimer for mgrherhrh
''')

page.components['button'].click([
  page.js.post("http://127.0.0.1:8080/viewer", datamap([page.components['date']], attrs={"button": 'Data 1'})).onSuccess([
    page.components['text'].build(events.data["message"])
  ]),
])

footer.style.css.padding_left = 110

# Specific to export to Angular
#app = angular.Angular(app_path=config.OUTPUT_PATHS_LOCALS_TS, name="angular")
#app.page(report=page, selector='app-root')
#app.publish()

