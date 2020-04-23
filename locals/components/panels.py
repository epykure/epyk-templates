
from epyk.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

p = rptObj.ui.panels.pills()
p.add_panel("Pill 1", rptObj.ui.col([rptObj.ui.text("test 1")]))
p.add_panel("Pill 2", rptObj.ui.col([rptObj.ui.text("test 2")]), selected=True)
p.add_panel("Pill 3", rptObj.ui.col([rptObj.ui.text("test 3")]))

tabs = rptObj.ui.panels.arrows_down()
tabs.add_panel("tab 1, this is something", rptObj.ui.col([rptObj.ui.text("test 1, this is for something")]))
tabs.add_panel("tab 2", rptObj.ui.col([rptObj.ui.text("test 2")]), icon="fab fa-500px")
tabs.add_panel("tab 3", rptObj.ui.col([rptObj.ui.text("test 3")]))


tabs = rptObj.ui.panels.arrows_up()
tabs.add_panel("tab 1, this is something", rptObj.ui.col([rptObj.ui.text("test 1, this is for something")]))
tabs.add_panel("tab 2", rptObj.ui.col([rptObj.ui.text("test 2")]))
tabs.add_panel("tab 3", rptObj.ui.col([rptObj.ui.text("test 3")]))


rptObj.ui.panels.sliding([
  rptObj.ui.col([rptObj.ui.text("test 2")])
], title="Sliding Panel")


rptObj.ui.panels.split(left=rptObj.ui.col([rptObj.ui.text("Left")]), right=rptObj.ui.col([rptObj.ui.text("Right")]))


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
