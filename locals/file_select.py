
from epyk.core.Page import Report
from epyk.tests import data_urls

import config


# Create a basic report object
rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
data = rptObj.py.requests.csv(data_urls.AIRPORT_TRAFFIC, store_location=config.OUTPUT_TEMPS)

select = rptObj.ui.select(data, column="airport")
multi = rptObj.ui.select(data, column="city", multiple=True)


lookupData = {"Akron-Canton Regional": [{"value": "A", 'text': "Example"}]}
select2 = rptObj.ui.lookup(lookupData)

#
select.change([
  c.write(select.dom.content),
  select2.build(select.dom.content)
], emtpyFncs=[
  c.write("emtpy"),
])


#
select2.change([
  #
  c.write(select2.dom.val, stringify=True),
])

c.move()

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_select"))