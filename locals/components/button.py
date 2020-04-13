
from epyk.core.Page import Report
import config

from epyk.core.js.packages import JsFontAwesome

# Defaults_css.Font.size = 20
# Create a basic report object
rptObj = Report()

# rptObj.ui.lists.list(["A", "B"])

#g = rptObj.ui.layouts.grid([t, t2, t3])

#rptObj.ui.button('toggle').click([
  #g.dom.panels, #.css("border", "1px solid black"),
#  g.dom.panel(3).toggle() # .css("border", "1px solid black")
#])


#ts = [rptObj.ui.text("test %s" % i) for i in range(5)]
#ts2 = [rptObj.ui.text("test %s" % i).css({"border": "1px solid black"}) for i in range(2)]
# tab = rptObj.ui.panels.tabs()
# for i in range(5):
#   tab.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i))
# #
# #
# sw = rptObj.ui.button("Ok")
# d = rptObj.ui.div().css({"border": "1px solid black"})

#t1 = rptObj.ui.text()
#t1.style.css.color = "green"
#t1.inReport = False
# htmlCode
# sw.click([
#   tab.dom.tab(3).firstChild.css({"color": 'red'}),
#   #tab.dom.add_tab("test"),,
#   #rptObj.js.objects.new(str(t1), isPyData=True, varName="obj"),
#   #d.dom.loadHtml(rptObj.js.objects.get("obj")),
#   #rptObj.js.console.debugger,
#   d.dom.loadHtml([
#     rptObj.ui.icon("fab fa-python"),
#     rptObj.ui.layouts.new_line()
#   ], append=True),
#   #t1.build("ok")
# ])

import random

cols, row = 10, 30
rec = []
for i in range(row):
  row = {}
  for j in range(cols):
    row["col_%s" % j] = random.randint(1, 100)
  rec.append(row)

simple_table = rptObj.ui.tables.grid(rec, cols=["col_%s" % i for i in range(int(cols/2))],
                                     rows=["col_%s" % i for i in range(int(cols/2), cols)])
# simple_table.add({"COL1": "Value", 'COL2': 'Field'})

#poly.animate("transform", "rotate", "0 190 50", "360 190 50")

#
# sw = rptObj.ui.buttons.switch({'on': "true", 'off': 'false'})
# sw.click([
#   rptObj.js.console.log(sw.content),
#   sw.dom.set_text("ok"),
# ])
# rptObj.ui.rich.update("Last update: ")
# cd = rptObj.ui.rich.countdown("2050-09-24")
# pre = rptObj.ui.texts.preformat("This is a pre formatted text")
# pre.style.css.border = "1px solid black"
# inp = rptObj.ui.input("")
#
# rptObj.ui.button("TEst").click([
#   rptObj.js.console.log(inp.dom.content),
#   pre.dom.append(inp.dom.content, new_line=True),
# ])
#
# d = rptObj.ui.div()
# d.style.css.width = 200
# d.style.css.height = 1200
# d.style.css.border = "1px solid black"
#
# i = rptObj.ui.images.icon(JsFontAwesome.ICON_ENVELOPE)
# c = rptObj.ui.texts.text("test glow")
# c.style.effects.glow("pink")
#
# d1 = rptObj.ui.div([i, c])
#
# b = rptObj.ui.texts.text("test blink")
# b.style.effects.blink()
#
# st = rptObj.ui.rich.stars(3, label="test", helper="This is a helper")
# st.click([
#   rptObj.js.console.log("data", skip_data_convert=True),
#   rptObj.js.navigator.geolocation.watchPosition("alert", "test")
# ])
#
#
# inp = rptObj.ui.input()
#
# ch = rptObj.ui.buttons.check(label="Label")
# ch.click(
#   ch.label.build(inp.dom.content)
# )
#
# rptObj.ui.buttons.mail().color("blue")
#
# rptObj.ui.buttons.check(True, label="Label")
# rptObj.ui.buttons.check(True, label="Label", icon="fas fa-align-center")

# c = rptObj.ui.div("ok")
#
# c.style.css.width = 100
# c.style.css.font_size = 80
# c.style.css.background_color = "white"
# c.style.css.height = 100
# c.style.css.color = 'yellow'
# # c.style.css.border = "1px solid black"
# c.style.css.border_radius = 100
# c.style.css.middle()
#
# c.style.css.shadow_box()
# c.style.css.shadow_text()

#c.style.css.sticky()
# c.style.effects.animate("pink", {"color": "blue", "width": "400px"})

#d += d1

# sw.style.css_class.keyframes("test", {
#   "50%": {"transform": "scale(1.5, 1.5)", "opacity": 0},
#   "99%": {"transform": "scale(0.001, 0.001)", "opacity": 0},
#   "100%": {"transform": "scale(0.001, 0.001)", "opacity": 1},
# })
#
# rptObj.ui.button("Ok").style.css_class.animation('test', {
#   "from": {"border-color": "white"},
#   "to": {"border-color": "red"},
# })

# ps += ts2


# for i in range(3):
#   ps += rptObj.ui.layouts.col([
#     rptObj.ui.text("test %s" % i),
#     rptObj.ui.text("test %s" % (i+1))])


#ps[1].css({"border": "1px solid black"})

#ps = rptObj.ui.layouts.row(ts)
#ps[1].css({"color": 'red'})

#rptObj.ui.button("Test").click([
#  ts[0].build("ok")
#])

rptObj.ui.buttons.zipfile("This is the data", "filename.txt")

# ps.title.style.css.color = "red"
#
# rptObj.ui.input("test")
# number = rptObj.ui.vignets.number(500, "Test")
#
# rptObj.ui.icons.github()
# rptObj.ui.icons.python()
# f = rptObj.ui.icons.facebook()
# i = rptObj.ui.icons.epyk()

# rptObj.ui.layouts.iframe("http://www.google.com")
#
# rptObj.ui.inputs.input()
#
# rptObj.ui.fields.input(label="test")
# rptObj.ui.fields.now(label="Time field")
# rptObj.ui.fields.cob(label="COB Date")
# rptObj.ui.fields.today(label="Date").selectable(["2019-09-01", "2019-09-06"])
# rptObj.ui.fields.textarea(label="Date")
# rptObj.ui.fields.password(label="password")
#
# rptObj.ui.slider(recordSet=[1, 2, 3, 4, 5, 6, 7])
#
# div = rptObj.ui.div([])
#
# b = rptObj.ui.button("add")
# b.click([
#   rptObj.js.alert(rptObj.js.navigator.language),
#   div.dom.jquery.load(r"./report_list.html")
# ])
#
#
# rptObj.ui.navigation.pin()
#
# rptObj.ui.buttons.switch()
# rptObj.ui.buttons.radio([{'value': 'test'}])
#
# rptObj.ui.texts.code("This is a code")
#
# rptObj.js.customFile("test.js")
#
# rptObj.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")
#
# rptObj.ui.navigation.indices(10)
#
# menu = rptObj.ui.layouts.icons(["fas fa-bell", "fas fa-calendar-check"])
# menu[0].click([menu[0].dom.css({"color": 'red'})])
#
#
# p = rptObj.ui.navigation.points(10)
# for i, _ in enumerate(p):
#   p.click(i, [])
#
# e = rptObj.ui.links.external('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})
# e.no_decoration
#
# data_link = rptObj.ui.links.data("link", "test#data")
# data_link.build({"text": 'new link Name', 'data': "new content"})
#
# b = rptObj.ui.button("Test")
# rptObj.ui.navigation.dots(10)
# rptObj.ui.navigation.points(10)
#b.options.multiple

#rptObj.ui.media.youtube("https://www.youtube.com/embed/dfiHMtih5Ac")

#rptObj.ui.sliders.progressbar(50)

#rptObj.ui.info("Test")
#rptObj.ui.rich.stars(3, label="test", helper="This is a helper")

#e = rptObj.ui.images.emoji(rptObj.symbols.smileys.DISAPPOINTED_FACE)
#e.style.css.font_size = 30
#print(e.style.css.attrs)

# records = [
#       {"label": 'python', 'value': 12},
#       {"label": 'Java', 'value': 5},
#       {"label": 'Javascript', 'value': 80}]
# rptObj.ui.charts.skillbars(records, y_column=['value'], x_axis=['label']).css({"width": '100px'})
#
# i = rptObj.ui.images.icon("fab fa-angellist")
# i.click(rptObj.js.alert(""))
#
# rptObj.ui.buttons.badge("test", 10, options={"badge_css": {"color": "white", "background-color": "red"},
#                         "badge_position": 'left'})
#
#
# b = rptObj.ui.button("test")
# print(b.style.classList)
# print(b.style.get_classes())

# d = rptObj.ui.div("Test")
# print(d.style.get_classes())

# p = rptObj.ui.layouts.panel([d])
#rptObj.style.add_classes.button.success()

#button = rptObj.ui.button("test")
#button.style.add_classes.external("youpi")
#button.style.add_classes.input.is_valid()
#success = button.style.define_classes.button.success()

#button.click(rptObj.js.alert(''))

#
# # Console component
# rptObj.ui.icons.facebook()
# rptObj.ui.icons.twitter()
# rptObj.ui.icons.linkedIn()
# rptObj.ui.icons.youtube()
#
# c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})
#
# i = rptObj.ui.icon("fas fa-bolt")
# div = rptObj.ui.div([i], width=(20, 'px')).css({"border": "1px solid black", "text-align": "center"})
# div.style.css_border_radius = "20px"
# div.style.css_background_color = "pink"
#
# div.style.animation(EffectsMoves.EffectsTranslate(), duration=3, timing_fnc="ease-out")
#
# b = rptObj.ui.button("test")
#
# # Simple button
#
# b.click([
#   rptObj.js.jquery.ajax("POST", 'https://jsonplaceholder.typicode.com/posts/1',
#                         successFncs=[
#                           b.build(rptObj.js.objects.result["title"]),
#                           "console.log(result)"]),
#   c.write(" **ok**, this is a test")])
#
# # Press Button
# b2 = rptObj.ui.button("test 2", width=100)
# b2.press(c.write(b2.dom.content + "' is locked'"))
#
#
# # Press Button and unlock
# b3 = rptObj.ui.button("test 3", width=100)
# b3.press(
#   c.write("Button 3 locked", timestamp=False),
#   c.write("Button 3 unlocked"))
#
# # Create a group of buttons
# b5 = rptObj.ui.button("test 5")
# b6 = rptObj.ui.button("test 6")
# b7 = rptObj.ui.button("test 7")
#
# # Change button CSS classes
# b8 = rptObj.ui.button("test 8")
# b8.style.clear() # Remove all CSS classes
# b8.css({"background-color": 'blue', 'color': 'white', 'border': 'None'})
#
# rptObj.ui.layouts.hr()
# # Create a CSS class
# b8_bis = rptObj.ui.button("test CSS Class")
# b8_bis.style.clear()
# css_cls = rptObj.style.cssCls("test_css", {"color": "orange"}, {"hover": {"color": 'red'}})
# b8_bis.style.cssCls("test_css")
#
# rptObj.ui.layouts.new_line(1)
# # Change button hover CSS style
# b9 = rptObj.ui.button("test 9")
# b9.color("red")
#
# # Button middle page
# b10 = rptObj.ui.button("test 10")
# rptObj.ui.div(b10).css({"text-align": 'center'})
#
# # Create a button with an icon
# b11 = rptObj.ui.button("test 11", icon="fab fa-python")
#
# # Buttons categories
b12 = rptObj.ui.lists.buttons(["test 15", "test 13", "test 14"])
# for i in b12:
#   i.press(
#     rptObj.js.console.log("test"),
#     [rptObj.js.console.log("unlock")])
#
# # Buttons categories (manual)
# b15 = rptObj.ui.button("test 15", options={"group": "test_group"})
# b16 = rptObj.ui.button("test 16", options={"group": "test_group"})
# b15.options.multiple = True
# b16.options.multiple = True
# b15.press(
#   rptObj.js.console.log("test"),
#   [rptObj.js.console.log("unlock")])
# b16.press(
#   c.write("Ok"),
#   rptObj.js.console.log("test"),
#   [rptObj.js.console.log("unlock")])
#
# rptObj.ui.layouts.new_line(2)
# # Get button status
# b4 = rptObj.ui.button("test 4")
# b4.click([
#   rptObj.js.console.log(b3.dom.val),
#   rptObj.js.console.log(b16.dom.val),
#   rptObj.js.console.log(b12[0].dom.val),
#   rptObj.js.console.log(b12[1].dom.content),
#   b3.build("Test") # Change value
# ]
# )
#
# # Events
#
# # Change a CSS Style
# b12[0].click([
#   b12[0].dom.css("color", "green")
# ])
#
# # go to another page
#
# # run a service
#
# # add attributes to the url
#
# rptObj.ui.layouts.new_line(1)
# # Other buttons types
rptObj.ui.icons.awesome(icon="fas fa-align-center", text="This is a text")
# rptObj.ui.layouts.new_line(1)
rptObj.ui.buttons.check(label="test")
rptObj.ui.buttons.radio(["A", "B"])
rptObj.ui.buttons.toggle({'on': "true", 'off': 'false'})
rptObj.ui.buttons.button('Confirm')
rptObj.ui.buttons.important('Important')
#
# c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
