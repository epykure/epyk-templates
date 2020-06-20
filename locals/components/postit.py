

from epyk.core.Page import Report

from epyk.tests import data_urls


page = Report()
page.headers.dev()

page.ui.layouts.new_line(10)

example = page.ui.title("Example")
text = page.ui.text("This is a text")
example.style.css.color = 'red'
data_rest = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
ts = page.ui.charts.chartJs.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date")

p = page.ui.postit([example, text, ts])
p.anchor.style.css.margin_left = '50px'
p.popup.style.css.height = "250px"
p.popup.style.css.width = "300px"
