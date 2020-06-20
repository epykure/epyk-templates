
import random

from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

data = []
for j in range(15):
  data.append( [random.randint(0, 10) for i in range(6)] )

button = page.ui.button("test")
p_map = page.ui.charts.plotly.maps([data])
p_map.data.contours.z.project.z = True

button.click([
  page.js.post("/data_plotly_3d").onSuccess([
    p_map.build(page.js.objects.data),
  ]),
])
