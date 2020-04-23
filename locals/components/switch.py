
from epyk.core.Page import Report

import config

rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

s1 = rptObj.ui.buttons.toggle({'on': "true", 'off': 'false'})

#
# wih an event
s2 = rptObj.ui.buttons.toggle({'on': "true", 'off': 'false'})
s2.click([
  rptObj.js.alert("Go to True")
],
  [
  c.dom.write("S2 => Back to false")
  ]
)
# In Sync with S2 changes
s3 = rptObj.ui.buttons.toggle({'on': "true", 'off': 'false'}, color='red')
s3.switch_label.style.css.width = 100

# Label is changing
s4 = rptObj.ui.buttons.toggle({'on': "true", 'off': 'false'})

# Different CSS Style
s5 = rptObj.ui.buttons.toggle({'on': "true", 'off': 'false'})
s5.switch_label.style.css.width = 40

# Click even
rptObj.ui.button("click").click([
  c.dom.write(s1.dom.content),

  # Change the label without changing the state of the component
  s4.dom.set_text("Correct"),
  s4.dom.set_text("Wrong", False)

])

# Rebuild S4 with new underlying values
rptObj.ui.button("Build S4").click([
  s4.build({'on': "Yes", 'off': 'No'})
])

# Toggle the state of the component
rptObj.ui.button("Force Selection").click([
  s4.js.toggle()
])

# Rebuild S4 and set it to True
rptObj.ui.button("Disable").click([
  s4.build({'on': "Yes", 'off': 'No'}),
  s4.js.true()
])

c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
