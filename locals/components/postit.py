

from epyk.core.Page import Report
from epyk.tests import data_urls

import config
rptObj = Report()
rptObj.headers.dev()

rptObj.ui.layouts.new_line(10)

example = rptObj.ui.title("Example")
text = rptObj.ui.text("This is a text")
example.style.css.color = 'red'
data_rest = rptObj.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES, store_location=config.OUTPUT_TEMPS)
ts = rptObj.ui.charts.chartJs.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")

p = rptObj.ui.postit([example, text, ts])
p.anchor.style.css.margin_left = '50px'
p.popup.style.css.height = "250px"
p.popup.style.css.width = "300px"

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)