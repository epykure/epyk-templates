"""
Create a bespoke HTML from a report runnable in a Node server.

This will require a Node server.
"""

if __name__ == '__main__':
  from epyk.core.Page import Report

  # The path to the Vue App
  out_path = r"C:\NodeJs"
  folder_target = r"views"

  page = Report()

  page.ui.text("#This is a text", options={"markdown": True})
  page.ui.button("This is a test").click([
    page.js.alert("test")
  ])

  app = page.outs.publish(server="node", app_path=out_path, module="MyModule", selector='mymodule',
                    target_folder=folder_target, auto_route=True)

  app.router(target_folder=folder_target) # inspect("MyModule", from_launcher=True)
  #app.launch("MyModule", target_folder=folder_target)