
import config
from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()

b = rptObj.ui.navbar(title="Epyk")
# b += rptObj.ui.link("Test")

content = rptObj.ui.contents(top=50)

t = rptObj.ui.title("test", 1)
t = rptObj.ui.title("test", 4)
t = rptObj.ui.title("test", 3)
t = rptObj.ui.title("test")

rptObj.ui.vignets.bubble({"value": 23.890, "title": "Title", 'url': '#'}, helper="This is a helper")
rptObj.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")
rptObj.ui.rich.stars(3, label="test", helper="This is a helper")
rptObj.ui.vignets.text({"title": "New Python Framework", 'value': "A new Python Web Framework", 'color': 'green',
                             'icon': 'fab fa-python', 'colorTitle': 'darkgreen'})
rptObj.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")
rptObj.ui.info("Test")
rptObj.ui.vignets.number(500, "Test")
rptObj.ui.rich.update("Last update: ")

rptObj.ui.title("test print")
rptObj.ui.rich.prism("print('test')")


# rptObj.ui.rich.countdown("2050-09-24")
#rptObj.ui.rich.blocktext({"text": 'This is a brand new python framework', "title": 'New Python Web Framework',
#                          "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_rich_text"))
