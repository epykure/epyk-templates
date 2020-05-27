
import sys
sys.path.append(r"../../epyk-ui")

from epyk.web import angular

app = angular.Angular(app_path=r"C:\Angular", name="my-first-app")

page = app.page(None, "test2", 'AppComponentTest2')

chartBarId = page.components.chart({'values': [10, 10, 60, 5], 'type': 'bar', 'labels': ["A", "B", "C", "D"]})
chartPieId = page.components.chart({'values': [10, 10, 60, 5], 'type': 'pie', 'labels': ["A", "B", "C", "D"]})
table = page.components.table({'values': [10, 10, 60, 5], 'type': 'pie', 'labels': ["A", "B", "C", "D"]})
print(chartBarId, chartPieId)

page.components.input()
page.components.button("Test", 'update', [page.http("getData", ["console.log(this.input.nativeElement.value); this.%s.update(data); this.%s.update(data)" % (chartBarId, chartPieId) ])])

#page.components.chart({'values': [10, 5, 2, 5], 'type': 'line', 'labels': ["A", "B", "C", "D"]})
#page.components.chart({'values': [10, 10, 60, 5], 'type': 'scatter', 'labels': ["A", "B", "C", "D"]})

app.publish()

#route = app.route
#route.add(component="AppTest", alias="test", path="./pr/app.component_test_new")

#app.ng_modules().add("HttpClientModule", '@angular/common/http')
#print( app.ng_modules() )
#route.export()
