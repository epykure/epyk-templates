"""
Create a bespoke HTML from a report runnable in a Deno server.

This will require a Deno server.
"""

if __name__ == '__main__':
  from epyk.core.Page import Report

  # The path to the Vue App
  out_path = r""
  folder_target = "views"

  page = Report()

  page.ui.text("#This is a text", options={"markdown": True})
  page.ui.button("This is a test").click([
    page.js.alert("test")
  ])

  page.outs.publish(server="deno", app_path=out_path, module="MyModule", selector='mymodule',
                    target_folder=folder_target, auto_route=True)
