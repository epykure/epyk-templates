
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

lt = page.ui.lists.box([
  {"text": 'test', 'color': 'green', 'title': 'This is a file', 'icons': [
    {"icon": 'fab fa-js', 'click': 'alert(value)', 'tooltip': 'test'},
    {"icon": 'fab fa-python', 'click': 'alert(value)'},
  ]},
  {"text": 'test', 'title': 'This is another file', 'icons': [
    {"icon": 'fab fa-js', 'click': 'alert(value)'},
    {"icon": 'fab fa-python', 'click': 'alert(value)'},
  ]}
], width=(200, 'px'))

button = page.ui.button("Add").click([
  lt.dom.add({"text": 'test', 'title': 'This is a file', 'icons': [
    {"icon": 'fab fa-js', 'click': 'alert(value)', 'color': 'red'},
    {"icon": 'fab fa-python', 'click': 'alert(value)'}
  ]})
])