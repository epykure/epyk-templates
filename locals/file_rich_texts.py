
import config
from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()

b = rptObj.ui.navbar(title="Epyk")
b.move()

# b += rptObj.ui.link("Test")

# Console component
c = rptObj.ui.rich.console("This is a log section for all the events in the different buttons *", options={"timestamp": True})

content = rptObj.ui.contents(top=50)
#
t = rptObj.ui.title("test", 1)
t = rptObj.ui.title("test", 4)
t = rptObj.ui.title("test", 3)
t = rptObj.ui.title("test")

content.move()
rptObj.ui.sliders.progressbar(40)
rptObj.ui.slider([1, 2, 3, 4, 5, 6, 7])

rptObj.ui.vignets.bubble({"value": 23.890, "title": "Title", 'url': '#'}, helper="This is a helper")
rptObj.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")
rptObj.ui.rich.stars(3, label="test", helper="This is a helper")
rptObj.ui.vignets.text({"title": "New Python Framework", 'value': "A new Python Web Framework", 'color': 'green',
                             'icon': 'fab fa-python', 'colorTitle': 'darkgreen'})
rptObj.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")
rptObj.ui.info("Test")
rptObj.ui.vignets.number(500, "Test")
rptObj.ui.rich.update("Last update: ")

number = rptObj.ui.vignets.number(500, "Test")
number_2 = rptObj.ui.vignets.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
number.span.add_icon(rptObj.ui.icons.get.ICON_ENVELOPE)

light = rptObj.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")

rptObj.ui.title("test print")

stars = rptObj.ui.rich.stars(3, label="test", helper="This is a helper")
stars.click()

rptObj.ui.rich.countdown("2020-09-24")
rptObj.ui.rich.update("Last update: ")

rptObj.ui.button("Click").click([
  c.dom.write(light.dom.val, stringify=True)
])


c.move()

# rptObj.ui.rich.countdown("2050-09-24")
#rptObj.ui.rich.blocktext({"text": 'This is a brand new python framework', "title": 'New Python Web Framework',
#                          "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_rich_text"))
