from epyk.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

t = rptObj.ui.text("Youpi")

rptObj.ui.button("Click").click([
  t.build("# hello, markdown!"),
  t.dom.content.fromMarkdown()
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)