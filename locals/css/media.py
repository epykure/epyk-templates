
import config
import PacthRunner

from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

div = rptObj.ui.div("toto")

div.style.css_class.media({div: {"background-color": "red"}}, 'only', 'screen', {"and": [{'max-width': '600px'}]})
div.style.css_class.media({div: {"background-color": "blue"}}, 'only', 'screen', {"and": [{'min-width': '800px'}]})

button = rptObj.ui.buttons.button('Contact Sales')
imp = rptObj.ui.buttons.important('Get Started for Free')
nav = rptObj.ui.navigation.bar(title="test")
nav.add_text("This is a huge text that I don't know what to do with")
nav + button
nav + imp

nav.style.css_class.media({nav: {"float": "none", 'width': '100%'}}, 'only', 'screen', {"and": [{'max-width': '600px'}]})

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)