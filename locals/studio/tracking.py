
from epyk_studio.core.Page import Report
from epyk.tests import mocks

# Create a basic report object
page = Report()
page.headers.dev()

value = 70

p = page.ui.percent().to(value)
p.style.css.font_factor(10)

stats = page.studio.col([
  page.studio.calendar.days(align="center"),
  page.ui.text("Result for this month"),
  p,
  page.ui.sliders.progressbar(0).to(70)
], position="top")

donut = page.studio.calendar.donut(mocks.languages, y_columns=["change"], x_axis="name", height=(200, "px"))
donut.chart.options.legend.display = False
radar = page.studio.calendar.radar(mocks.languages, y_columns=["change"], x_axis="name", height=(200, "px"))
radar.chart.options.legend.display = False

page.studio.title("Activity Tracking", align="center")
charts = page.studio.col([
  page.studio.title("Category Tracking", align="center"),
  page.studio.row([donut, radar]),
  page.studio.title("Weekly Tracking", align="center"),
  page.studio.dashboard.bar(mocks.languages, y_columns=["change"], x_axis="name", height=(200, "px"))
])

page.studio.row([stats, charts], position="top")

