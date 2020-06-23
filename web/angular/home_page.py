"""
Change the Angular App home page
"""


if __name__ == '__main__':
  from epyk.core.Page import Report
  from epyk.web import angular

  page = Report()

  page.ui.text("#This is a text", options={"markdown": True})
  page.ui.button("This is a test").click([
    page.js.alert("test")
  ])

  # Link the report to a Angular Python object
  node_app = angular.Angular(r"C:\Angular")
  node_app.home_page(page, "angular-apps2")
