
from epyk.core.Page import Report


page = Report()
page.headers.dev()

page.ui.div("{{ name }}").css({"color": 'red'})
