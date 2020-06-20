import config

from epyk.core.Page import Report


# Create a basic report object
page = Report()

page.ui.text("#This is a text", options={"markdown": True})
page.ui.button("This is a test").click([
  page.js.alert("test")
])

#page.components.chart({'values': [10, 5, 2, 5], 'type': 'line', 'labels': ["A", "B", "C", "D"]})
#page.components.chart({'values': [10, 10, 60, 5], 'type': 'scatter', 'labels': ["A", "B", "C", "D"]})

page.outs.publish(server="vue", app_path=config.OUTPUT_PATHS_LOCALS_TS, module=config.OUT_FILENAME, selector='app-root')

#route = app.route
#route.add(component="AppTest", alias="test", path="./pr/app.component_test_new")

#app.ng_modules().add("HttpClientModule", '@angular/common/http')
#print( app.ng_modules() )
#route.export()
