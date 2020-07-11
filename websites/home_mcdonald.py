# https://www.mcdonalds.com/gb/en-gb/menu/reduced-menu.html

from epyk.core.Page import Report

# TODO
# - Add style in the tabs

page = Report()
page.headers.favicon("https://image.flaticon.com/icons/svg/732/732217.svg")
page.headers.title("Reduce Menu")

navbar = page.ui.navbar(logo="https://www.mcdonalds.com/content/dam/uk/nfl/logo/logo-80.png", height=(100, 'px'), options={"status": False})
navbar.style.css.border_bottom = None

impage_path = "https://www.mcdonalds.com/is/image/content/dam/uk/nfl/nutrition/nfl-product/menu/products/%s?$Category_Desktop$"
row = []
for picture in ["mcdonalds-Mayo-Chicken.jpg", "mcdonalds-Bacon-Mayo-Chicken.jpg", "mcdonalds-Bacon-Double-Cheeseburger.jpg", "mcdonalds-Big-Mac.jpg"]:
  row.append(page.ui.images.background(url=impage_path % picture))

section = page.ui.titles.head("Reduced Menu", align="center")
section.style.css.color = "black"

menu = page.ui.col([section, page.ui.row(row)])

tabs = page.ui.panels.tabs()
for name in ["Menu", "My McDonald's app", "McDelivery", "Latest Updates"]:
  tabs.add_panel(name, menu if name =="Menu" else page.ui.div(), selected=name =="Menu")

