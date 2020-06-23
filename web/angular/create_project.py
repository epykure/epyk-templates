"""
Set up the Angular views directly from your Epyk packages.

The below will run the necessary functions in order to

1. Create the Application from the Node.Js server
2. Add the necessary package (optional)
3. Automatically link the new view to a route
4. Start the server
"""


if __name__ == '__main__':
  from epyk.web import angular

  node_app = angular.Angular(r"C:\Angular")
  angular_name = "angular-apps2"

  # Create the Angular App
  #node_app.create(angular_name)

  # Install the packages but also update the angular.json automatically
  #node_app.cli(angular_name).npm(["jquery", "jquery-ui-dist"])

  #node_app.router(angular_name)

  node_app.serve(angular_name)
