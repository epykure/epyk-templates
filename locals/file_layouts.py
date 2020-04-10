
from epyk.core.Page import Report
from epyk.tests import test_statics
from epyk.core.css import Defaults

from epyk.core.css.themes import ThemeDark

#
#Defaults.BACKGROUND = None
Defaults.BODY_CONTAINER = {"border": None}

# Create a basic report object
rptObj = Report()
rptObj.theme = ThemeDark.Dark()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

rptObj.ui.layouts.iframe("http://www.google.com")

#
# dd = rptObj.ui.icon("fas fa-arrow-down").css({"border": '1px solid black', "position": 'fixed', "width": 'none',
#                    "border-radius": '20px', "padding": '8px', "right": '20px'})
#
# du = rptObj.ui.icon("fas fa-arrow-up").css({"border": '1px solid black', "position": 'fixed', "width": 'none',
#                    "border-radius": '20px', "padding": '8px', "right": '20px', "bottom": "20px"})
#
#
# dd.style.addCls("CssDivOnHoverBackgroundLight")
# du.style.addCls("CssDivOnHoverBackgroundLight")

#rptObj.ui.navigation.down()
rptObj.ui.navigation.pin("test")

# du = rptObj.ui.navigation.to(100, tooltip="test")
#
# ind = rptObj.ui.navigation.indices(10)
#
# p = rptObj.ui.navigation.points(10)
# d = rptObj.ui.navigation.dots(10)
#
# p.options.background_color = "orange"
# b = rptObj.ui.button("test")
#
# for i, _ in enumerate(p):
#   p.click(i, [b.build(rptObj.js.objects.this), rptObj.js.console.log(rptObj.js.objects.this.getAttribute("data-position"))])
#   d.click(i, [])
#   ind.click(i, [])

# tab = rptObj.ui.layouts.pills()
# tab.add_panel("test", rptObj.ui.div("Test Content"))
# tab.add_panel("test 2", rptObj.ui.div("Test Content 2"))


# tab2 = rptObj.ui.layouts.tabs()
# tab2.add_panel("test", rptObj.ui.div("Test Content"))
# tab2.add_panel("test 2", rptObj.ui.layouts.col([
#   rptObj.ui.div("Test Content 3")]))


# fixed = rptObj.ui.layouts.slide([], title="This is a title")
# fixed += rptObj.ui.title("Sub title")
#fixed.title.click([
#  rptObj.js.getElementsByName("panel_%s" % fixed.htmlId).first.toggle()
#])

#div = rptObj.ui.layouts.panelsplit(left=number, right=number_2, resizable=True)
#div = rptObj.ui.layouts.tabs([number, number_3, number_2, number_4])

# rptObj.ui.layouts.dialogs()

rptObj.ui.layouts.hr()

rptObj.ui.layouts.new_line(5)

for i in range(70, 100):
  t = rptObj.ui.text("this [test](http://www.google.com) !(fab fa-python) --is-- ***an*** *example*, **ok**", options={"limit_char": i})
  t.options.markdown = True
  #rptObj.js.addOnLoad(t.refresh())

rptObj.ui.layouts.new_line(50)

# d.drop([
#   rptObj.js.objects.data.toRecord([1, 2, 3, 4], "result"),
#   c.write(rptObj.js.objects.event.dataTransfer.text)
# ])

#
# du.click([
#   c.write("ok")
# ])

t = rptObj.ui.text("Test")
t.click([
  rptObj.js.objects.event.stopPropagation(),
  rptObj.js.objects.event.preventDefault(),
  c.dom.write("Message from the text box"),
])

rptObj.ui.images.badge("306", url="google", icon="fas fa-align-center", options={'badge_css': {'color': 'white', "background": 'red'}})
rptObj.ui.images.badge("306", url="google", icon="fas fa-align-center", options={'badge_css': {'color': 'white', "background": 'orange'}})
rptObj.ui.images.badge("306", url="google", icon="fas fa-align-center", options={'badge_css': {'color': 'white', "background": 'red'}})
rptObj.ui.images.badge("306", url="google", icon="fas fa-align-center", options={'badge_css': {'color': 'white', "background": 'red'}})
b = rptObj.ui.images.badge(7688, icon="fab fa-python", options={'badge_css': {'color': 'white', "background": 'red'}})
b.options.badge_css = {"background": 'green'}

i = rptObj.ui.layouts.icons(["fas fa-align-center", 'fab fa-python'])
i.icon.click([i.icon.dom.css({"color": 'red'})])

#d + t

#rptObj.js.addOnLoad(
#  rptObj.js.window.events.addContentLoaded(rptObj.js.alert("DOM fully loaded and parsed"))
  #rptObj.js.window.addEventListener("scroll", rptObj.js.alert(rptObj.js.window.scrollY))
#)

c.move()

rptObj.headers.title("title")
rptObj.headers.favicon('https://github.com/favicon.ico')
rptObj.headers.meta.custom('language', 'python')
print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_layouts"))
