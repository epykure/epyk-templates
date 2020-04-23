
from epyk.core.Page import Report
from epyk.core.html import Html
import config


class MyBody(Html.Body):
  def set_content(self, report, page_content):
    left = report.ui.div()
    but = report.ui.button("Click")
    but.click([
      report.js.alert("Test")
    ])
    left += but
    left.style.css.color = "white"
    right = report.ui.div("right")
    center = report.ui.div(page_content)
    div = report.ui.row([left, center, right])
    div[0].attr["class"].add("col-1")
    div[0].style.css.background_color = "grey"
    div[2].attr["class"].add("col-1")
    text = report.ui.text("text")
    text.inReport = False
    div.inReport = False
    self._html_content = "%s%s" % (div.html(), text.html())
    return self


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

rptObj.body = MyBody

p = rptObj.ui.sliders.progressbar(30)
rptObj.ui.date()
t = rptObj.ui.fields.today()
#t.selectable(["2019-09-01", "2019-09-06"])
ti = rptObj.ui.fields.now()
# s = rptObj.ui.slider(recordSet=[1, 2, 3, 4, 5, 6, 7])

b = rptObj.ui.button("Get")

b.click([
#  rptObj.js.alert(s.dom.inViewPort),
  #rptObj.js.alert(rptObj.js.viewHeight),
  #rptObj.js.alert(t.dom.content),
  #rptObj.js.alert(p.dom.content),
  #rptObj.js.alert(s.dom.content),
  #rptObj.js.alert(ti.input.dom.content),
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
