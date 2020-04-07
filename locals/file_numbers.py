
from epyk.core.Page import Report

import config

rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
n = rptObj.ui.numbers.digits(76862.095)
n.style.color = "red"


n1 = rptObj.ui.text(76862.095)

#
delta = rptObj.ui.charts.plotly.number_with_delta(2009860)
delta.data.delta.reference = 400
delta.data.vmax = 400
delta.data.gauge.shape = "bullet"
delta.data.delta.valueformat = ".0f"
delta.data.domain([0, 0.5], [0, 0.5])
delta.data.add_title("<b style='color:red'>test</b>")

n1.onReady([
  n1.dom.format.number.toFixed(6)
])

rptObj.ui.button("display").click([
  rptObj.js.alert(n1.dom.content.number.toFixed(5)),
  c.write(n1.dom.val, stringify=True, format="Number: %s")
])

#
rptObj.ui.button("click").click([
  n1.build(-38866),
  n1.dom.format.toMoney('£')
])

c.move()

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_numbers"))
