
from epyk.core.Page import Report

page = Report()
page.headers.dev()

select = page.ui.select([])
select.ajax('/select', options={'preserveSelected': False, 'requestDelay': 50})
