
import config

from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Create a grid
grid1 = rptObj.ui.grid()

# Change the style of the main container
grid1.style.css.border = "1px solid black"

# Add a row to the grid
grid1 += [1, 2, 3]

# Apply still changes on all the row
for c in grid1[0]:
  c.style.color = 'green'
  # Change the div container created as cells were not html components
  c.val[0].style.css.text_align = "center"

# Change the size of one cell in the row
grid1[0][1].set_size(8)
grid1[0][1].style.background = 'yellow'

# Add a name properties to some cells in the row
grid1[0][0].set_attrs({"name": 'special_cell'})
grid1[0][2].set_attrs({"name": 'special_cell'})

# CSS class
# Create a bespoke CSS class for this report
from epyk.core.css.styles.classes import CssStyle

class MyCellCls(CssStyle.Style):
  _attrs = {'background': 'white', 'color': 'red', 'cursor': 'pointer'}
  _hover = {'background': 'red', 'color': 'white'}

  _selectors = {'child': '[name=special_cell]'}

# Attach the class to the component
# The color red will be replaced by the inline style green attached to each cell in the row
grid1.style.add_classes.custom(MyCellCls)

# Add second row
grid1 += [1, 2, 3]

for c in grid1[1]:
  c.set_attrs({"name": 'special_cell'})
  c.val[0].style.css.text_align = "center"

# Add event
grid1[1][0].click([
  #
  rptObj.js.console.log(grid1[1][0].val[0].dom.content),
  # Hide row
  grid1[0].dom.toggle(),
  # Change value of row
  grid1[0][1].build("new value")
])

# create a container with a row and columns
col2 = rptObj.ui.col([
  rptObj.ui.div("Text 1"),
  rptObj.ui.div("Text 2"),
])

text = rptObj.ui.div("Text 3")
grid2 = rptObj.ui.grid([
  [text, col2]
]).css({"border": '1px solid black'})

# Change the background style of the first column
grid2[0][0].style.css.background = 'green'

# hide colon (and rescale)
rptObj.ui.button("Toggle Panel").click([
  grid2.dom.togglePanel(1)
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)