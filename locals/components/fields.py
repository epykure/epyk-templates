
import config

from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()

a = rptObj.ui.fields.select(["Apple", 'Orange'], label="test", helper="select fruit", options={"align": 'center'})#
a.input.attr["data-live-search"] = "true"

rptObj.ui.fields.date('2020-04-08', label="Date").included_dates(["2020-04-08", "2019-09-06"])

rptObj.ui.fields.today(label="Date").included_dates(["2019-09-01", "2019-09-06"])

rptObj.ui.fields.now(label="timestamp", color="red", helper="This is the report timestamp")

rptObj.ui.fields.time(label="timestamp", color="red", helper="This is the report timestamp")

rptObj.ui.fields.input("", label="Range Example", icon="fas fa-unlock-alt")

rptObj.ui.fields.input("", label="Range Example", icon="fas fa-unlock-alt")

rptObj.ui.fields.static(label="readonly field")

rptObj.ui.fields.integer(label="test")

rptObj.ui.fields.password(label="password")

rptObj.ui.fields.textarea(label="Date")

rptObj.ui.fields.checkbox(True, label="Check")

rptObj.ui.fields.radio(False, label="Radio")

rptObj.ui.fields.range(54, min=20, label="Range Example", icon="fas fa-unlock-alt")

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
