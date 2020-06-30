
from epyk.core.Page import Report
from epyk.core.data import http


# Defaults_css.Font.size = 20
# Create a basic report object
page = Report()
page.headers.dev()

bc = page.ui.breadcrumb([
  {"text": 'part 1', 'url': 'part1'},
  {"text": 'part 2', 'url': 'part2'},
  {"text": 'part 3', 'url': 'part3'},
])

# This will change the link of part 2 and part 3 and add some extra information in the link
# epyk-templates/outs/html/locals_components_breadcrumb.html?type=howto
bc.onReady([
  bc[1].dom.setAttribute("href", http.get("type").toString().prepend("part2?")),
  bc[2].dom.setAttribute("href", http.get("type").toString().prepend("http://www.w3schools.com/").add("/howto_css_breadcrumbs.asp"))
])

