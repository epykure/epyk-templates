
from epyk.core.Page import Report#

import config

rptObj = Report()

rptObj.ui.title("Python (programming language)", level=1)

rptObj.ui.texts.paragraph('''
Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, 
Python's design philosophy emphasizes code readability with its notable use of significant whitespace. 
Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[28]
''')
print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="web_wikipedia"))
