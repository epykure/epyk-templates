

from epyk.core.Page import Report
import config

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

records = [
  {"label": 'python', 'value': 12},
  {"label": 'Java', 'value': 5},
  {"label": 'Javascript', 'value': 80}]
rptObj.ui.charts.skillbars(records, y_column='value', x_axis='label').css({"width": '100px'})

records = [["title 1", "title 2"], [True, 2], [3, 4]]
table = rptObj.ui.layouts.table(records)
table.style.clear()
for cell in table.col(0):
  cell.css({"color": 'red'})

#table.row(i=1)[1].css({"background": 'green'})
#table.row(i=1)[0].set_html_content(rptObj.ui.rich.light(table.row(i=1)[0].val, label="ok", tooltip="test"))
#table.add([2, 87])

records = [
  {"test": "test"},
  {"test": "test"},
]

# triangle = rptObj.ui.charts.svg.triangle(100).css({"animation-name": 'spin', "animation-duration": '5000ms',
#                                         "animation-iteration-count": 'infinite', "animation-timing-function:": 'linear'})


#triangle.style.animation(effect=EffectsMoves.EffectsSpin(), duration=3)

# rptObj.style.keyframes(name="spin", attrs={
#     "from": {"transform": "rotate(0deg)"},
#     "to": {"transform": "rotate(360deg)"}
# })

div = rptObj.ui.div().css({"width": "20px", "border-radius": "10px"})
div + rptObj.ui.icon("fas fa-adjust")
#div.style.addCls("CssIconHoverEffect")

# from epyk.core.css.effects import EffectsHover
#
# EffectsHover.EffectsHoverEcho
#
# rptObj.style.keyframes(name="test", attrs={
#   "50%": {"transform": "scale(1.5, 1.5)", "opacity": 0},
#   "99%": {"transform": "scale(0.001, 0.001)", "opacity": 0},
#   "100%": {"transform": "scale(0.001, 0.001)", "opacity": 1},
# })

#rptObj.ui.buttons.badge("test", 10, options={"badge_css": {"color": "white", "background-color": "red"}, "badge_position": 'left'})

d = rptObj.ui.div("").css({"background-color": "black", "color": 'white'})
d + rptObj.ui.div("test").css({"background-color": "grey", "width": "100px", "text-align": 'center', "display": "inline-block"})
d + rptObj.ui.div("test").css({"background-color": "blue", "width": "50px", "text-align": 'center', "display": "inline-block"})
d + rptObj.ui.div("test").css({"background-color": "blue", "width": "50px", "text-align": 'center', "display": "inline-block"})
d + rptObj.ui.div("test").css({"background-color": "blue", "width": "50px", "text-align": 'center', "display": "inline-block"})

rptObj.ui.panels.sliding(rptObj.ui.tables.grid(records, rows=["test"], cols=["A", "B", "C", "D", "E", "F"]), title="Test Sliding")
rptObj.ui.panels.sliding(rptObj.ui.tables.grid(records, rows=["test"], cols=["A", "B", "C", "D", "E", "F"]), title="Test Sliding")

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
