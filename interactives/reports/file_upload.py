
from epyk.core.Page import Report
from epyk.core.data import datamap


page = Report()
page.headers.dev()


page.ui.layouts.br(10)
drop_file = page.ui.network.dropfile()

input = page.ui.input(htmlCode="test")
drop_file.drop([
  drop_file.transfer("/file")
], jsData=datamap([input], attrs={"value": 'test'}))