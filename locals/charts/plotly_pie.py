
import config

from epyk.core.Page import Report

rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

pie = rptObj.ui.charts.plotly.pie()
pie.data.values = [2, 3, 4, 4]
pie.data.type = "pie"
pie.data.textinfo = "label+percent"
pie.data.textposition = "outside"
pie.data.automargin = True
pie.data.labels = ["Wages", "Operating expenses", "Cost of sales", "Insurance"]
pie.layout.no_background()
pie.data.outsidetextfont.color = 'blue'

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
