
import os
import random

from epyk.core.Page import Report


# Create a basic report object
rptObj = Report()
rptObj.headers.dev()

data = []
for j in range(15):
  data.append( [random.randint(0, 10) for i in range(6)] )

button = rptObj.ui.button("test")
p_map = rptObj.ui.charts.plotly.maps([data])
p_map.data.contours.z.project.z = True

button.click([
  rptObj.js.post("/data_plotly_3d").onSuccess([
    p_map.build(rptObj.js.objects.data),
  ]),
])

rptObj.outs.html_file(path="./../front_end", name=os.path.basename(__file__)[:-3])