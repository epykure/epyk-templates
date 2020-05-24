
import sys
sys.path.append(r"../../epyk-ui")

from epyk.web import angular

#npms = angular.requirements(rptObj)
app = angular.app(r"C:\Angular\test-app")#
app.npm(["chartjs-plugin-zoom"])
#app.ng("test-app").lint() #.generate('component', 'test')

#app.npm(npms)
#app.install()