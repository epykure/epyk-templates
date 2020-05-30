
from epyk.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

# c = rptObj.ui.charts.svg.heart(w=100, h=200, fill="pink")
# c[0].transform("transform", "rotate", "0 100 10", "360 100 100")
# c.text("Aurelie", 50, 100)

#svg = rptObj.ui.charts.svg.new()
#svg.path().line_to(15, 8).line_to(0, 15)
#svg.path(10, 20).line_to(200, 200).horizontal_line_to(10).vertical_line_to(150).move_to(200, 100)

rptObj.ui.charts.svg.arrow_left(y1=40)

svg = rptObj.ui.charts.svg.axes()
m = svg.defs().marker("circle", "0 0 10 10", 5, 5)
m.circle(5, 5, 5, 'red')
m.markerWidth(10).markerHeight(10)
p = svg.path(0, 0, from_origin=True).line_to(50, 100).\
  horizontal_line_to(300).\
  line_to(400, 200).smooth_quadratic_bezier_curve_to(50, 50)
p.markers(m.url)

#
# poly = rptObj.ui.charts.svg.rectangle(50, 50, 50, 50, rx=20, ry=20)
# poly[0].transform("transform", "rotate", "0 100 100", "360 100 100")
# poly.css({"margin": '10px', "border": "1px solid black"})
#
# poly.text("Ok", 50, 50)
# poly[-1].transform("transform", "rotate", "0 100 100", "360 100 100")
# poly[-1].line("New line", 50, 60)
#
# defs = poly.defs()
# gradients = defs.radialGradient("gradient_test")
# gradients.stop("20%", {"stop-color": "pink", "stop-opacity": 1})
# gradients.stop("95%", {"stop-color": "green", "stop-opacity": 1})
# m = defs.marker("arrow", "0 0 10 10", 5, 5)
# m.circle(5, 5, 5, 'red')
# ma = defs.marker("arrow_arrow", "0 0 10 10", 5, 5)
# ma.arrow()
# ma.markerWidth(10).markerHeight(10)
#
# poly.line(1, 20, 20, 30)
# pl = poly.polyline([(15, 80), (29, 50), (43, 60), (57, 30), (71, 40), (85, 15)])
# pl.markers(ma.url)
#
#
# poly[0].fill(gradients.url)
#
# poly.circle(20, 50, 3, fill=gradients.url)
# poly.ellipse(20, 40, 10, 20)
# poly.polygon([(20, 60), (40, 19), (16, 19), (100, 100)], fill=gradients.url) # .css({"fill": gradients.url})
# g = poly.g()
# # f = poly.foreignObject(10, 20, "100%", 150)
# # f.add([
# #     rptObj.ui.texts.label("Test Label").css({"color": 'red'}),
# #     rptObj.ui.input()
# # ])
#
# g.css({"stroke": 'blue'})


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)