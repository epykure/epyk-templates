import sys
sys.path.append(r"C:\Users\nelso\PycharmProjects\epyk-ui")

from epyk.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

d = rptObj.ui.fields.today('test')
i = rptObj.ui.fields.input(placeholder='test2', label='test1')
i2 = rptObj.ui.fields.input('test3', label='test2')
form_modal = rptObj.ui.modal.forms([d, i, i2], "http://127.0.0.1:5000", "POST")
rptObj.ui.buttons.button('SHOW').click(form_modal.show())

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_popup"))
