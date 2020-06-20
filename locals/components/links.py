
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

page.ui.inputs.label("test")

#
page.ui.links.external('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})
page.ui.layouts.new_line(2)

#
page.ui.links.button('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})
page.ui.layouts.new_line(2)

#
page.ui.link("Profiling results", url='#')
page.ui.layouts.new_line(2)

#
l = page.ui.links.link('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})
b = page.ui.images.badge("new")
l.append_child(b)
page.ui.layouts.new_line(2)

#
data_link = page.ui.links.data("link", "test#data")
data_link.build({"text": 'new link Name', 'data': "new content"})
page.ui.layouts.new_line(2)

