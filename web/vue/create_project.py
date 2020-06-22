"""
Set up the Vue.Js views directly from your Epyk packages.

The below will run the necessary functions in order to

1. Create the Application from the Node.Js server
2. Change the Linter default options to remove the error with Epyk JavaScript
3. Add the necessary package (optional)
4. Automatically link the new view to a route
5. Start the server
"""


if __name__ == '__main__':
  from epyk.web import vue

  node_app = vue.VueJs(r"C:\VueJs")
  vue_name = "vue-apps-new"

  # Create the vue application from the NodeJs server
  #node_app.create(vue_name)

  # Change the linter to remove
  #node_app.cli(vue_name).linter()

  #
  #node_app.cli(vue_name).npm(["jquery", "jquery-ui-dist"])
  #node_app.cli(vue_name).add_router()

  #node_app.serve(vue_name)


