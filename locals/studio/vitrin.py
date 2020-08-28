
from epyk_studio.core.Page import Report

# Create a basic report object
page = Report()
page.headers.dev()

page.body.style.css.padding = "0 10%"

page.studio.button("test")

row = page.ui.row(position="top", align="center")
for i in range(6):
  row.add(page.studio.vitrine.image("https://colorlib.com/preview/theme/photographer/img/portfolio/%s.jpg" % (i+1)))
  row[-1].style.effects.rotate()

#image.style.effects.zoom()

t = page.ui.text("test")

filp = page.studio.wedding.flip("Front Side", "Back Side", height=(100, "px"))

p = page.studio.vitrine.picture("https://colorlib.com/preview/theme/photographer/img/portfolio/23.jpg", filp)
p.style.add_classes.screens.no_phone()

t.style.css.color = 'red'
l = page.studio.vitrine.list([
  "test",
  t

])
l.style.add_classes.screens.font()


page.studio.vitrine.subscribe()