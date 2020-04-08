from epyk.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

t = rptObj.ui.text("Youpi")

rptObj.ui.button("Click").click([
  t.build("# hello, markdown!"),
  t.dom.content.fromMarkdown()
])

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_dates"))