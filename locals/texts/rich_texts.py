
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

b = page.ui.navbar(title="Epyk")
b.move()

# b += page.ui.link("Test")

# Console component
c = page.ui.rich.console("This is a log section for all the events in the different buttons *", options={"timestamp": True})

content = page.ui.contents(top=50)
#
t = page.ui.title("test", 1)
t = page.ui.title("test", 4)
t = page.ui.title("test", 3)
t = page.ui.title("test")

content.move()
page.ui.sliders.progressbar(40)
page.ui.slider([1, 2, 3, 4, 5, 6, 7])

page.ui.vignets.bubble({"value": 23.890, "title": "Title", 'url': '#'}, helper="This is a helper")
page.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")
page.ui.rich.stars(3, label="test", helper="This is a helper")
page.ui.vignets.text({"title": "New Python Framework", 'value': "A new Python Web Framework", 'color': 'green',
                             'icon': 'fab fa-python', 'colorTitle': 'darkgreen'})
page.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")
page.ui.info("Test")
page.ui.vignets.number(500, "Test")
page.ui.rich.update("Last update: ")

number = page.ui.vignets.number(500, "Test")
number_2 = page.ui.vignets.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
number.span.add_icon(page.ui.icons.get.ICON_ENVELOPE)

light = page.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")

page.ui.title("test print")

stars = page.ui.rich.stars(3, label="test", helper="This is a helper")
stars.click()

page.ui.rich.countdown(day=24, month=9, year=2020)
page.ui.rich.update("Last update: ")

page.ui.button("Click").click([
  c.dom.write(light.dom.val, stringify=True)
])


c.move()

# page.ui.rich.countdown("2050-09-24")
#page.ui.rich.blocktext({"text": 'This is a brand new python framework', "title": 'New Python Web Framework',
#                          "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})

