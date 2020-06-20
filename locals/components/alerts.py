
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()


danger = page.ui.network.warning()

button = page.ui.button("Show")
button.click([
  danger.build('''
  ###New 
alert
  ''')
])
