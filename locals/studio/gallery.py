
from epyk_studio.core.Page import Report

import os


# Create a basic report object
page = Report()
page.headers.dev()

picture_path = None

page.ui.div([
  page.ui.title("More than", align="center"),
  page.ui.euro(1000).to(2000),
  page.ui.text("recipes", align="center"),
], width=("auto", ""))

num = page.ui.euro().to(50)
bar = page.ui.sliders.progressbar(50).to(70)

page.ui.button("Test").click([
  num.dom.to(1000),
  bar.dom.to(100),
])

title = page.studio.text("Canteen")
title.style.css.font_factor(30)
title.style.css.margin_top = 20
title.style.css.color = "white"
title.style.css.font_family = 'Meddon'


h = page.studio.gallery.heroes("IMG_6752.JPG", path=picture_path)
h.add(title)

im = page.studio.gallery.overlay("33c33735-8a1e-4bef-8201-155b4775304a.jpg", "test caption", path=picture_path)
im.style.effects.colored()

page.studio.row([
page.studio.gallery.overlay("33c33735-8a1e-4bef-8201-155b4775304a.jpg", "test caption", path=picture_path),
page.studio.gallery.overlay("33c33735-8a1e-4bef-8201-155b4775304a.jpg", "test caption", path=picture_path, options={"direction": 'bottom'}),
page.studio.gallery.overlay("33c33735-8a1e-4bef-8201-155b4775304a.jpg", "test caption", path=picture_path, options={"direction": 'top'})
])
picts = []
for f in os.listdir(picture_path):
  if f.endswith(".jpg"):
    picts.append(f)

page.studio.row([
  page.studio.col([
    page.studio.title("Starters"),
    page.studio.gallery.link("33c33735-8a1e-4bef-8201-155b4775304a.jpg", path=picture_path)]),
  page.studio.col([
    page.studio.title("Mains"),
    page.studio.gallery.link("00c13627-3e12-4954-9506-60f9ba55a89b.jpg", path=picture_path)]),
  page.studio.col([
    page.studio.title("Desserts"),
    page.studio.gallery.link("1d4befb5-7e86-4160-8f79-324fe3a46116.jpg", path=picture_path)]),
])
dishes = page.studio.text("Her specialities", align="center")
dishes.style.css.font_factor(30)
dishes.style.css.margin_top = 20
dishes.style.css.font_family = 'Meddon'

pic = page.studio.blog.picture("", path=picture_path, align="center")
pic.style.css.width = "calc(80% - 20px)"
pic.style.css.border_radius = 20

test = page.ui.text("THis is a test", align="center")
test.style.css.margin_top = 10
test.style.css.margin_bottom = 10
recipe = page.ui.button("Recipe", align="center")

cont = page.ui.div([pic, test, recipe])
cont.style.css.padding_top = 10
cont.style.css.padding_bottom = 10

p = page.ui.layouts.popup([cont])
p.options.top = 0
#p.container_max_height(150)
p.add_title("This is a title")

moz = page.studio.gallery.mosaic(picts, path=picture_path)
for i, r in enumerate(moz.pictures):
  # todo: bar price
  # Todo: add title url
  r.parent.add(page.studio.shop.bar("Test", 39.5, "This is a test", url="www.google.fr", options={"name": '_self'}).css({"margin": '0 5px', 'width': '100%'}))
  r.click([
    pic.build(r.dom.content),
    test.build(r.dom.content),
    p.dom.show()])

page.studio.gallery.pagination(10)

q = page.studio.blog.quote('''
The best cuisine I have ever tasted in my life
''', "Anonymous", '(husband)', width=80, align="center")
#q.style.css.margin = "auto 20%"


chef_title = page.studio.title("About the Chef")

a = page.studio.vitrine.avatar("00c13627-3e12-4954-9506-60f9ba55a89b.jpg", size=150, path=picture_path)
ca = page.studio.div([chef_title])
ca.add([a])
#ca.style.css.margin = "auto 10%"

burgers = page.studio.text("Burgers", align="center")
burgers.style.css.font_factor(30)
burgers.style.css.margin_top = 20
burgers.style.css.font_family = 'Meddon'
p1 = page.studio.blog.picture("3499b882-bbdd-4fb5-b028-32a7f5a88f79.jpg", path=picture_path, width=(600, 'px'), height=(300, 'px'),
label='''Double cheese burgers!''')

page.studio.gallery.fixed("54a2a939-9898-4997-bb87-9e71b3bcf9ae.jpg", path=picture_path)

s = page.studio.vitrine.price(8.52, 'Standard', ["**20** Websites", '**400000** URLS per accounts'], url="#").css({"margin-bottom": '10px'})
b = page.studio.vitrine.price(18.52, 'Business', ["**20** Websites", '**400000** URLS per accounts']).css({"margin-bottom": '10px'})
p = page.studio.vitrine.price(28.52, 'Prenium', ["**20** Websites", '**400000** URLS per accounts']).css({"margin-bottom": '10px'})
row = page.studio.row([s, b, p], position="top")
row.style.css.margin_top = 20
