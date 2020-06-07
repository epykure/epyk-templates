
import config
from epyk.core.Page import Report


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()


container = rptObj.ui.network.chat(htmlCode='chat_service')


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)