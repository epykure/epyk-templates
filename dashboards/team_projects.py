
from epyk.core.Page import Report

from epyk.core.data import events
from epyk.core.data import datamap


# Create a basic report object
page = Report()
page.headers.dev()

import random

page.ui.titles.head("Team KPI")
page.ui.timelines.milestone("2020-07-05")
page.ui.timelines.meeting(15)
page.ui.timelines.categories()
page.ui.timelines.workload(9)
page.ui.network.upload()
page.ui.inputs.file([
])

rows = []
#rows.append(page.ui.row(["Category", "", "Timelines", "Progression", "", "", "", "Status", "Activity", "Files"]))
rows.append(["Category", "", "Timelines", "Progression", "", "", "", "Status", "Activity", "Files"])

for i in range(10):
  rows.append([
    page.ui.div("This is a text").css({"border-left": '1px solid %s' % page.theme.success[1], 'padding-left': '10px',
                                         'background': page.theme.success[0]}),
    page.ui.icons.avatar(r"test.jpg", name="Test"),
    page.ui.timelines.view("2020-01-05", "2020-%s-%s" % (random.randint(1, 12), random.randint(1, 25))),
    page.ui.sliders.progress(random.randint(1, 100)),
    page.ui.icons.awesome("fab fa-angular"),
    page.ui.icons.badge(random.randint(1, 20), icon="fab fa-angular"),
    page.ui.buttons.small("Click"),
    page.ui.rich.light('red'),
    page.ui.charts.sparkline("line", [random.randint(1, 25) for i in range(10)], width=("40", 'px')),
    page.ui.network.download("quakes.csv", path=r"C:\U\Downloads")
    #page.ui.rich.status("In Progress jj")
  #, width=(1000, 'px')
  ])

grid = page.ui.grid(rows)
grid.style.css.margin_top = 10

# page.ui.row(

# for row in rows:
#   row[0].set_size("col-2")
#   row[1].set_size("auto")
#   row[2].set_size("col-2")
#   row[3].set_size("col-2")
#   row[4].set_size("auto")
#   row[6].set_size("auto")
#   row[7].set_size("auto")
#   row[8].set_size("auto")

