
from epyk.core.Page import Report
import config

# Create a basic report object
rptObj = Report()

rptObj.ui.charts.sparkline("box", [1, 2, 3, 4, 5, 4, 3, 2, 1])
rptObj.ui.charts.sparkline("bar", [1, 2, 3, 4, 5, 4, 3, 2, 10])

rptObj.ui.charts.sparkline("bar", [1, 2, 3], title="Top Clients (#)",  options={"barWidth": 20})

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
