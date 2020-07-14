# https://www.w3schools.com/w3css/tryw3css_templates_wedding.htm
# https://www.theknot.com/gs/wedding-websites

# TODO
# - List items
# - Images carrousel
# = manage accents
# - banner
# - nav bar


from epyk.core.Page import Report#
from websites.material import theknot_data


page = Report()
page.headers.favicon(theknot_data.FAVIRON)
page.headers.title(theknot_data.TITLE)

the_knot = page.ui.text(theknot_data.NAME)
nav = page.ui.navbar(logo=the_knot)
nav.style.css.border_bottom = None
nav.style.css.position = "None"

button_style = {"font-size": '16px', "background": "#e96150", 'border': "1px solid #e96150", 'color': "white", 'padding-top': "6px",
                "padding-bottom": "6px", 'margin-top': "10px"}
margin = "30px"

bg = page.ui.images.background(theknot_data.BACKGROUND_1, height=(500, 'px'))
bg.style.css.color = "white"

slogan = page.ui.text(theknot_data.SLOGAN, width=(60, "%"))
slogan.style.css.font_size = "50px"
slogan.style.css.display = "inline-block"
slogan.style.css.margin_top = 60
bg.add(slogan)

content = page.ui.text(theknot_data.MAIN_TEXT, width=(60, "%"))
content.style.css.display = "inline-block"
content.style.css.font_size = "20px"
bg.add(content)

button = page.ui.button(theknot_data.START_BUTTON, width=(150, 'px')).css(button_style)
button.style.css.margin_left = "20%"
bg.add(button)

members = page.ui.text(theknot_data.LOGIN_TEXT, width=(60, "%"))
members.style.css.display = "inline-block"
members.style.css.font_size = "20px"
bg.add(members)

row = []
for rec in theknot_data.BOXES:
  row.append(page.ui.col([
    page.ui.titles.title(rec['title']).css({"text-align": 'center'}),
    page.ui.text(rec['content'], align="center")], align="center"))
page.ui.row(row, width=(90, '%'), align="center").css({"margin-top": margin, "margin-bottom": margin})

page.ui.banners.title(title=theknot_data.BANNER_1['title'], content=theknot_data.BANNER_1['content'],
  background="#f5f6f8").css({"margin-top": margin, "margin-bottom": margin})
b2 = page.ui.button(theknot_data.BUTTON_DESIGN, align="center").css(button_style)

page.ui.vignets.image(
  title="The Easiest Set-Up Ever",
  content="Because syncing your registries and personalizing a free wedding website seriously should be this simple.",
  image="https://media-api.xogrp.com/images/929612c1-78e5-43d4-ab9e-528f9b24d276~rs_560.h"
).css({"margin-top": margin, "margin-bottom": margin})

page.ui.vignets.image(title=theknot_data.VIGNET_1['title'], content=theknot_data.VIGNET_1['content'],
  image=theknot_data.VIGNET_1['image'], options={"picture": 'right'}).css({"margin-top": margin, "margin-bottom": margin})

page.ui.vignets.image(title=theknot_data.VIGNET_2['title'], content=theknot_data.VIGNET_2['content'],
  image=theknot_data.VIGNET_2['image']).css({"margin-top": margin, "margin-bottom": margin})

page.ui.banners.title(title=theknot_data.BANNER_TITLE['title'], content=theknot_data.BANNER_TITLE['content'], background="#f5f6f8")

row = []
for v in theknot_data.VIGNETS:
  image = page.ui.vignets.image(title=v["title"], render="col", image=v["image"], height=(500, 'px'))
  image.style.css.border = "1px solid #d6d6d6"
  row.append(image)
row_vignets = page.ui.row(row, width=(80, "%"), align="center")
row_vignets.style.css.background = "#f5f6f8"
row_vignets.css({"margin-top": margin, "margin-bottom": margin})

page.ui.banners.title(title=theknot_data.BANNER_TITLE_1['title'], content=theknot_data.BANNER_TITLE_1['content'])
page.ui.banners.title(title=theknot_data.BANNER_TITLE_2['title'], content=theknot_data.BANNER_TITLE_2['content'])

rows, row = [], []
for ct in theknot_data.CONTENTS:
  row.append(page.ui.vignets.vignet(title=ct["title"], icon=ct["icon"], content=ct["content"], render="col", width=(100, "%")))
  if len(row) == 4:
    rows.append(row)
    row = []
if row:
  rows.append(row)
grid = page.ui.grid(rows, width=(80, "%"))

page.ui.banners.title(title=theknot_data.BANNER_TITLE_3['title'], content=theknot_data.BANNER_TITLE_3['content'])

b2 = page.ui.button(theknot_data.BUTTON_BESPOKE, align="center").css(button_style)

page.ui.banners.text(theknot_data.TEXT_PHOTOS, width=(80, "%"), size_notch=-2)
