
import config

from epyk.core.Page import Report

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Add the file from the local environment context defined in Imports.STATIC_PATH
# This path will be overridden and specific to your configuration
rptObj.js.customFile("test.js")

# https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/core.min.js
rptObj.js.customFile("crypto-js.min.js", path='https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0')

# Add a bespoke Javascript fragment at the begining of the report
rptObj.js.customText("console.log('The devil is in the detail')")

# Or this example use a function from the module crypto.
# More details about the Javascript library here: https://github.com/brix/crypto-js
rptObj.js.customText("console.log(CryptoJS.SHA256('Message'))")

# Even if it is not recommanded it is also possible to define Javascript functions
rptObj.js.customText("function myJsFnc(data){ return data + 10}")

# And to use it in any Javascript event
rptObj.ui.button("Click").click([
  # Skip the conversion to not consider it as a Python String
  rptObj.js.console.log("myJsFnc(5)", skip_data_convert=True),

  # It is also possible to add this fragment directly in the function by using Javascript objects primitives
  # In this example the function is anonymous
  rptObj.js.console.log(rptObj.js.objects.get("(function(data){return data + 20})(5)"))
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
