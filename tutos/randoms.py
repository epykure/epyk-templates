
from epyk.core.Page import Report
from epyk.core.js import expr

from interactives.links.RandServices import ResRand

# Create a basic report object
page = Report()
page.body.style.css.background = "linear-gradient(45deg, #00f 1%, #fff 1%, #fff 49%, #00f 49%, #00f 51%, #fff 51%, #fff 99%, #00f 99%)"
page.body.style.css.background_size = "20px 20px"
page.body.style.css.background_position = "0 0"
page.body.style.css.padding = "0 10%"
page.body.style.css.min_height = "100%"

container = page.ui.div(width=(100, '%'), height=(100, '%'))
container.style.css.background = "white"
container.style.css.padding = "0 10px"

title = page.ui.titles.head("Pseudorandom Number Generator in Python")
title.style.css.display = "inline-block"
container.add(title)

paragraph = page.ui.texts.paragraph('''
The Mersenne Twister is a pseudorandom number generator (PRNG). It is by far the most widely used general-purpose PRNG.[1] Its name derives from the fact that its period length is chosen to be a Mersenne prime.

The Mersenne Twister was developed in 1997 by Makoto Matsumoto [ja] (松本 眞) and Takuji Nishimura (西村 拓士).[2] It was designed specifically to rectify most of the flaws found in older PRNGs.

The most commonly used version of the Mersenne Twister algorithm is based on the Mersenne prime 219937−1. The standard implementation of that, MT19937, uses a 32-bit word length. There is another implementation (with five variants[3]) that uses a 64-bit word length, MT19937-64; it generates a different sequence.
''')
container.add(paragraph)

sub_title = page.ui.titles.title("Parameters")
container.add(sub_title)

seed1 = page.ui.fields.input(label="seed", htmlCode="seed")
container.add(seed1)

n = page.ui.fields.input(label="Samples", htmlCode="n")
container.add(n)

valid = page.ui.buttons.normal("Run Python")
valid_js = page.ui.buttons.normal("Run Javascript")
valid_js.style.css.margin_left = 10
container.add(page.ui.div([valid, valid_js]))

py_title = page.ui.titles.title("Python Results")
container.add(py_title)

line = page.ui.charts.chartJs.line([], y_columns=["y"], x_axis=["x"])
bar = page.ui.charts.chartJs.bar([], y_columns=["y"], x_axis=["x"])
container.add(page.ui.row([line, bar]).css({"background": 'white'}))

hr = page.ui.layouts.hr()
js_title = page.ui.titles.title("Javascript Results")
container.add(hr)
container.add(js_title)
js_line = page.ui.charts.chartJs.line([], y_columns=["y"], x_axis=["x"])
container.add(js_line)

# Call the Python function
valid.click([
  page.js.objects.time("window.time_py"),
  page.js.post("http://127.0.0.1:8080/%s" % ResRand.end_point, [seed1, n]).onSuccess([
    line.build(ResRand().random),
    bar.build(ResRand().random),
    page.js.console.perf("window.time_py", label="Python Processing: "),
    page.js.print("Python computed", 2000, cssAttrs={"bottom": "10px", 'right': "10px", 'position': 'fixed'})
  ]),
])

# Pure Javascript implementation
valid_js.click([
  page.js.objects.list.new([], "js_data"),
  page.js.objects.time("window.time_py"),
  expr.for_(n, [
    page.js.objects.new({}, "row"),
    page.js.objects.get("row").setattr("y", page.js.math.random()).r,
    page.js.objects.get("row").setattr("x", page.js.objects.get("i")).r,
    page.js.objects.list.get("js_data").push(page.js.objects.get("row"))
  ]),
  js_line.build(page.js.objects.list.get("js_data")),
  page.js.console.perf("window.time_py", label="Javascript Processing: "),
  page.js.print("Javascript computed", 2000, cssAttrs={"bottom": "10px", 'right': "10px", 'position': 'fixed'})
])
