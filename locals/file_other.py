
from epyk.core.Page import Report



# Create a basic report object
page = Report()

wf = page.ui.workflow([{"status": 'red', 'value': 'ok', 'label': 'ok'}, {"status": 'green', 'value': 'ok 2', 'label': 'ok'}])

page.body.set_background()

b = page.ui.button("Click")

page.ui.context_menu([])
# def test(a):
#   return {}
#
# header = {'Content-Type': 'application/x-www-form-urlencoded'}
# page.ui.button('test').click([
#   page.js.request_http("ajax", "POST", "https://api.cdnjs.com/libraries").setHeaders(header).onSuccess([
#     page.js.alert(page.js.objects.request.get("ajax").responseText)]).send(encodeURIData={"search": 'ractive'})
#
# ])

