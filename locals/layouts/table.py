
import config

from epyk.core.Page import Report
from epyk.core.css.themes import ThemeDark

# Create a basic report object
rptObj = Report()

tb1 = rptObj.ui.layouts.table()
tb1.style.css.border_collapse = "separate"
tb1.style.css.border_spacing = 10

# Add a header (first row is by default the header)
tb1 += [1, 2, 3]

# Change the CSS style of a cell in the header
tb1.get_header()[1].style.color = 'red'
tb1.get_header()[1].style.background = 'grey'

# Change all header cells style
for c in tb1.get_header():
  # This will add CSS attribute to the CSS inline section
  c.style.padding = 5
  c.style.border = "1px solid black"

# Create bespoke HTML component to be added to the table
span1 = rptObj.ui.texts.span("Text 1")
span2 = rptObj.ui.texts.span("Text 2")
span3 = rptObj.ui.texts.span("Text 3")

# Add the row to the table (to the body)
tb1 += [span1, span2, span3]
span3.click([
  rptObj.js.log(span3.dom.content),
  span2.build("New text"),

  # Change the cell properties
  tb1[1][1].dom.css({"background": rptObj.theme.warning[0]})
])

# Add an extra row to the header
tb1.header += [4, 5]
tb1.get_header(1)[1].colspan(2)
tb1.get_header(1)[1].style.border = "1px solid black"

# Add a text caption to this table
text = tb1.add_caption("This is a text attached to the table")
text.style.css.text_align = 'left'

# CSS class
# Create a bespoke CSS class for this report
from epyk.core.css.styles.classes import CssStyle

class MyCssBody(CssStyle.Style):
  _attrs = {'background': 'inherit'}
  _hover = {'background': rptObj.theme.success[0]}

  _selectors = {'child': 'tbody td'}

# Attach the class to the component
tb1.style.add_classes.custom(MyCssBody)

# add row


# delete row


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)