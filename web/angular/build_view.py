"""
Create a bespoke Vue from a report.

This will require the vue settings.
"""

if __name__ == '__main__':
  from epyk.core.Page import Report

  # The path to the Angular App
  out_path = r"C:\Angular\angular-apps2"
  folder_target = r"src\views"

  page = Report()

  page.ui.text("#This is a text", options={"markdown": True})
  page.ui.button("This is a test").click([
    page.js.alert("test")
  ])

  page.outs.publish(server="angular", app_path=out_path, module="MyModule", selector='mymodule', target_folder=folder_target, auto_route=True)
