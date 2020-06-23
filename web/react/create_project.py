"""
Set up the React views directly from your Epyk packages.

The below will run the necessary functions in order to

1. Add the React CLI
2. Create the React Application from the Node.Js server
2. Add external packages
3. Automatically link the new view to a route
4. Start the server
"""


if __name__ == '__main__':
  from epyk.web import react

  node_app = react.React(r"C:\React")
  react_name = "react-apps"

  # Install React CLI
  #node_app.clis.react()

  # Create the Angular App
  #node_app.create(react_name)

  # Install the packages but also update the angular.json automatically
  #node_app.cli(angular_name).npm(["jquery", "jquery-ui-dist"])

  #node_app.router(react_name)

  #node_app.serve(react_name)
