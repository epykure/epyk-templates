# https://www.mcdonalds.com/gb/en-gb/good-to-know/in-our-restaurants/my-mcdonalds-app.html

from epyk.core.Page import Report#
from websites.material import mcdonal_data

page = Report()
page.headers.favicon(mcdonal_data.FAVICON)
page.headers.title(mcdonal_data.TITLE)

navbar = page.ui.navbar(logo=mcdonal_data.LOGO, height=(100, 'px'), options={"status": False})
navbar.style.css.border_bottom = None

content = page.ui.div([])
content.add(page.ui.text(mcdonal_data.TEXT).css({"margin-bottom": '10px'}))
content.add(page.ui.buttons.store(mcdonal_data.GOOGLE_PLAY['image'], mcdonal_data.GOOGLE_PLAY['link']))
content.add(page.ui.buttons.store(mcdonal_data.APPLE_STORE['image'], mcdonal_data.APPLE_STORE['link']))

page.ui.vignets.image(title=mcdonal_data.APP_IMAGE['title'], content=content, image=mcdonal_data.APP_IMAGE['image'])
page.ui.banners.title(title=mcdonal_data.APP_BANNER_TITLE['title'], content=mcdonal_data.APP_BANNER_TITLE['content'])

row = []
for v in mcdonal_data.VIGNETS:
  image = page.ui.vignets.image(title=v["title"], render="col", image=v["image"], content=v["content"], height=(500, 'px'))
  image.style.css.border = "1px solid #d6d6d6"
  row.append(image)
row_vignets = page.ui.row(row, width=(80, "%"), align="center")
page.ui.banners.title(title=mcdonal_data.APP_BANNER_TITLE_2['title'], content=mcdonal_data.APP_BANNER_TITLE_2['content'])

items = page.ui.div()
for link in mcdonal_data.APP_LINKS:
  items.add(page.ui.link(link))
page.ui.panels.sliding([items], mcdonal_data.APP_SLIDING_PANEL_TITLE)