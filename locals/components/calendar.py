
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

content = {
  "2020-07-02": {
    'task1': 50,
    'task2': 50
  },
  "2020-07-03": {
    'task1': 100,
  },
  "2020-07-21": {
    'task4': 100
  },
  "2020-07-22": {
    'task4': 100
  }
}

page.ui.titles.headline("Daily")
july = page.ui.calendars.days(7, content, align="center", options={"colors": {"task4": 'red'}})

july.task('task1', start="2020-07-10", capacity=[50, 30, 10, 80])
july.task('task3', start="2020-07-20", capacity=[50, 40, 10])


page.ui.calendars.legend(july.tasks)

july.style.css.margin = "0 5px"

august = page.ui.calendars.forecast(4, content, options={"colors": {"task4": 'red'}})
august.style.css.margin = "0 5px"

#page.ui.row([july, august], position="top")

page.ui.titles.headline("Montly")
monthly = page.ui.calendars.months(align="center")
monthly.style.css.margin_top = 10

update = page.ui.rich.update()

page.ui.button("Click").click([
  update.refresh()
])