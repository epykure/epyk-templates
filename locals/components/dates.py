from epyk.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

rptObj.ui.date()
rptObj.ui.fields.today()

rptObj.ui.button("Click").click([

])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)