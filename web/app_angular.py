
import config

from epyk.web import angular

app = angular.Angular(app_path=config.OUTPUT_PATHS_LOCALS_TS, name="angular")

page = app.page()
page.components.button("test")

#page.components.chart({'values': [10, 5, 2, 5], 'type': 'line', 'labels': ["A", "B", "C", "D"]})
#page.components.chart({'values': [10, 10, 60, 5], 'type': 'scatter', 'labels': ["A", "B", "C", "D"]})

app.publish()

#route = app.route
#route.add(component="AppTest", alias="test", path="./pr/app.component_test_new")

#app.ng_modules().add("HttpClientModule", '@angular/common/http')
#print( app.ng_modules() )
#route.export()
