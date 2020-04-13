
from epyk.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

rptObj.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")
rptObj.ui.texts.up_down({'previous': 240885, 'value': 240985})

number = rptObj.ui.vignets.number(500, "Test")
number.span.add_icon(rptObj.ui.icons.get.ICON_ENVELOPE)

number_2 = rptObj.ui.vignets.number(500, "Test 2 ", options={"url": "http://www.google.fr"})

rptObj.ui.layouts.new_line()

rptObj.ui.div([number, number_2])

rptObj.ui.vignets.block({"text": 'This is a brand new python framework', "title": 'New Python Web Framework',
                         "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})

v = rptObj.ui.vignets.text({"title": "New Python Framework", 'value': "A new Python Web Framework", 'color': 'green',
                        'icon': 'fab fa-python', 'colorTitle': 'darkgreen'})

v.click(c.dom.write(v.dom.content))

rptObj.ui.vignets.bubble({"value": 23, "title": "Title"}, helper="This is a helper")

c.move()

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_bespoke"))
