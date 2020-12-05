from epyk_studio.core.Page import Report
from epyk.core.css.themes import ThemeBlue
from epyk.tests import data_urls
from epyk.core.js import std
from epyk.core.data import datamap


page = Report()
page.theme = ThemeBlue.BlueGrey()

world = page.ui.geo.chartJs.choropleths.world()

title = page.ui.title("COVID Map")
title_country = page.ui.title()

bar = page.ui.charts.chartJs.bar([], ['Confirmed', 'Deaths', 'Recovered'], 'Country/Region')
bar.options.scales.y_axis().ticks.toNumber()
bar.options.tooltips.callbacks.labelNumber()

row = page.ui.row([world, [title_country, bar]])
row.set_size_cols(9)

# Create a container for the HTML page
box = page.studio.containers.box()
box.extend([title, row])
box.style.standard()

# Group data for the processing on the JavaScript side
grp = page.data.js.record(std.var("covidData", global_scope=True)).filterGroup("aggData")
grp2 = page.data.js.record(std.var("covidData", global_scope=True)).filterGroup("aggData2")

world.click([
  title_country.build(world.activePoints().label),
  bar.build(grp.match(datamap(attrs={"Country/Region": world.activePoints().label})).group().sumBy(["Deaths", 'Confirmed', 'Recovered'], ["Country/Region"], cast_vals=True))
])

page.body.onReady([
  std.var("covidData", value=[], global_scope=True),
  page.js.d3.csv(data_urls.COUNTRY_WISE_COVID).records(std.var("covidData", global_scope=True)).then([
    world.build(grp2.group().sumBy(["Deaths"], ["Country/Region"], cast_vals=True).to_dict('Country/Region', 'Deaths'))
  ])
])