# https://www.mcdonalds.com/gb/en-gb/menu/reduced-menu.html

from epyk.core.Page import Report
from websites.material import mcdonal_data

# TODO
# - Add style in the tabs

page = Report()
page.headers.favicon(mcdonal_data.FAVICON)
page.headers.title(mcdonal_data.TITLE_HOME)

navbar = page.ui.navbar(logo=mcdonal_data.LOGO, height=(100, 'px'))
navbar.style.css.border_bottom = None

row = [page.ui.images.background(url=mcdonal_data.PICTURE_PATH % picture) for picture in mcdonal_data.MENU_ITEMS]
section = page.ui.titles.head(mcdonal_data.TITLE_REDUCE_MENU, align="center")
section.style.css.color = "black"
menu = page.ui.col([section, page.ui.row(row)])
tabs = page.ui.panels.tabs()
for name in mcdonal_data.MENU_TAB:
  tabs.add_panel(name, menu if name ==mcdonal_data.MENU_TAB_SELECTED else page.ui.div(), selected=name == mcdonal_data.MENU_TAB_SELECTED)

