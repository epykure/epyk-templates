
from epyk.core.Page import Report
import config


# Create a basic report object
rptObj = Report()


rptObj.ui.inputs.label("test")

#
rptObj.ui.links.external('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})
rptObj.ui.layouts.new_line(2)

#
rptObj.ui.links.button('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})
rptObj.ui.layouts.new_line(2)

#
rptObj.ui.link({"text": "Profiling results", "url": '#'})
rptObj.ui.layouts.new_line(2)

#
l = rptObj.ui.links.link('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})
b = rptObj.ui.images.badge("new")
l.append_child(b)
rptObj.ui.layouts.new_line(2)

#
data_link = rptObj.ui.links.data("link", "test#data")
data_link.build({"text": 'new link Name', 'data': "new content"})
rptObj.ui.layouts.new_line(2)


print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_link"))
