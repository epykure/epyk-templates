

from epyk.core.Page import Report


page = Report()
page.headers.dev()

contents = page.ui.contents("Contente")

page.body.onReady([
  contents.build([
    {"anchor": '#test', 'level': 1, 'text': 'Ok'}
  ])
])