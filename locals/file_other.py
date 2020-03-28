import sys
sys.path.append("../../epyk-ui")

from epyk.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

wf = rptObj.ui.workflow([{"status": 'red', 'value': 'ok', 'label': 'ok'}, {"status": 'green', 'value': 'ok 2', 'label': 'ok'}])

rptObj.body.set_background()

b = rptObj.ui.button("Click")

rptObj.ui.context_menu([])
# def test(a):
#   return {}
#
# header = {'Content-Type': 'application/x-www-form-urlencoded'}
# rptObj.ui.button('test').click([
#   rptObj.js.request_http("ajax", "POST", "https://api.cdnjs.com/libraries").setHeaders(header).onSuccess([
#     rptObj.js.alert(rptObj.js.objects.request.get("ajax").responseText)]).send(encodeURIData={"search": 'ractive'})
#
# ])


print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_others"))
