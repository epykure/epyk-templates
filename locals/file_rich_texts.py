
import config
from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()

b = rptObj.ui.navbar(title="Epyk")
# b += rptObj.ui.link("Test")

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

content = rptObj.ui.contents(top=50)

t = rptObj.ui.title("test", 1)
t = rptObj.ui.title("test", 4)
t = rptObj.ui.title("test", 3)
t = rptObj.ui.title("test")

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

light = rptObj.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")

rptObj.ui.title("test print")
rptObj.ui.rich.prism("print('test')")

stars = rptObj.ui.rich.stars(3, label="test", helper="This is a helper")
stars.click()

rptObj.ui.rich.countdown("2020-09-24")
rptObj.ui.rich.update("Last update: ")

rptObj.ui.button("Click").click([
  c.write(light.dom.content)
])

c.move()

# rptObj.ui.rich.countdown("2050-09-24")
#rptObj.ui.rich.blocktext({"text": 'This is a brand new python framework', "title": 'New Python Web Framework',
#                          "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_rich_text"))
