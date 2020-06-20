
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

data = [
  {"value": 'value', 'items': [
      {"value": 'value 1'},
      {"value": 'value 2', 'items': [
        {"value": 'value 3'},
      ]},
  ]}
]

d = page.ui.lists.dropdown(data)
d.click([
  page.js.console.log(page.js.objects.value)
])

