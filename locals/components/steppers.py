
from epyk.core.Page import Report

import config

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Stepper data
records = []
for i in range(6):
  records.append({'status': 'success', "tooltip": "test", 'value': 'test', 'title': 'Ok %s' % i},)

# Create a stepper
sp = rptObj.ui.stepper(records)

# Add a new shape to the list of existing ones
sp.add_shape("oval", '''
var shape = document.createElementNS(svgns, 'ellipse');
shape.setAttribute('stroke', options.backgrounds[status]);
shape.setAttribute('stroke-width', 1);
shape.setAttribute('cx', width / options.circle_factor );
shape.setAttribute('cy', height / options.circle_factor );
shape.setAttribute('rx', width / options.circle_factor );
shape.setAttribute('ry', height / options.circle_factor );
''')

# Add Event on the second item on the first stepper
sp.onReady([
  sp.dom[1].css({"cursor": "pointer"}),
  sp.dom[1].click(rptObj.js.alert("ok")),
])

# Change the color of the labels
sp.options.text_style['color'] = 'red'

# Create a new stepper with arrows
sp_a = rptObj.ui.steppers.arrow(records)

# New data set
v_records = []
for i in range(3):
  v_records.append({'status': 'success', "tooltip": "test", 'value': 'test', 'title': 'Item %s' % i})

# Create a vertical stepper
sp_v = rptObj.ui.steppers.vertical(v_records, shape='rectangle')
content = rptObj.ui.div("")

# Put the stepper in a container
rptObj.ui.row([sp_v, content])

# Add event on the stepper items
sp_v[0].click([content.build("value 1")])
sp_v[1].click([content.build("value 2")])
sp_v[2].click([content.build("value 3")])

# Event on the stepper
rptObj.ui.button("test").click([
  rptObj.js.window.setInterval([sp.dom[0].blink()], 'blink', milliseconds=1000),
  sp.dom[1].triangle(),
  sp.dom[2].rectangle('pending'),
  #sp.dom[3].arrow('pending'),
  sp.dom[0].circle(),
  sp.dom[0].text("Text 1"),
  sp.dom[2].text("Text 2"),
  sp.dom[1].text("Text 3"),
  rptObj.js.console.log(sp.dom[2].status),

  sp.dom[3].waiting(),
  #sp.dom.delete(0),
])

rptObj.ui.button("get status").click([
  rptObj.js.console.log(sp.dom[3].status),
  sp.dom.getByLabel("Ok 1").triangle(),

  # Add a new item using the new shape
  sp.dom.addItem("New Item", shape="oval", status='success')
])

rptObj.ui.button("Add Text").click([
  sp_v.dom.getByLabel("Item 0").text("Value"),

])

new_records = []
for i in range(6):
  new_records.append({'status': 'success', "tooltip": "test", 'value': 'test', 'title': 'New %s' % i},)

rptObj.ui.button("Build").click([
  sp.build(new_records),
  rptObj.js.window.clearInterval('blink')

])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
