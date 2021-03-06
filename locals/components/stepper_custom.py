
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

# Stepper data
records = []
for i in range(6):
  records.append({'status': 'success', "tooltip": "test", 'value': 'test', 'title': 'Ok %s' % i, 'label': 'Label %s' % i},)

# Create a stepper
sp = page.ui.stepper(records)
sp.options.line = False

# Add a new shape to the list of existing ones
# sp.add_shape("oval", '''
# var shape = document.createElementNS(svgns, 'ellipse');
# shape.setAttribute('stroke', options.backgrounds[status]);
# shape.setAttribute('stroke-width', 1);
# shape.setAttribute('cx', width / options.circle_factor );
# shape.setAttribute('cy', height / options.circle_factor );
# shape.setAttribute('rx', width / options.circle_factor );
# shape.setAttribute('ry', height / options.circle_factor );
# ''')
#

sp.add_shape("oval", '''
var shape = document.createElementNS(svgns, 'circle');
shape.setAttribute('stroke', options.backgrounds[status]);
shape.setAttribute('stroke-width', 1);
shape.setAttribute('cx', width / (options.circle_factor * 2) );
shape.setAttribute('cy', height / options.circle_factor  );
shape.setAttribute('r', height / (options.circle_factor * 2) );


var newText = document.createElementNS("http://www.w3.org/2000/svg", "text");
newText.setAttributeNS(null, 'x', (width / 2) +'px');
newText.setAttributeNS(null, 'y', (height / 2) + 5 +'px');
var textNode = document.createTextNode(step.label);
newText.appendChild(textNode);

svg.appendChild(newText)

''')

page.ui.button("Test").click([
  sp.dom[0].rectangle(),
  sp.dom[1].triangle(),
  sp.dom[2].circle(),
  sp.dom[3].arrow(),
])
