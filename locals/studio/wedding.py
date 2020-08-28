
from epyk_studio.core.Page import Report

# Create a basic report object
page = Report()
page.headers.dev()

page.body.style.globals.size = 20

t = page.ui.text("This is a test as an example")
t.style.effects.blink()

page.studio.wedding.theme()

num = page.ui.vignets.number(64897.5595, "Pages vues par jour", options={'label': 'after', 'symbol': 'T'})
num.click([
  num.link.build("15985632.415")
])
page.studio.events.progress(20)

#dist = page.py.geo.distance()
#print(dist)

page.studio.wedding.dated("2020-08-01", "Test", align="center")

tick = page.ui.pictos.tick(border="orange")
tick.click([
  page.js.alert("Ok")
])

page.studio.wedding.button("test")

vote = page.studio.shop.vote(3456)
vote.up.click([
  page.js.alert("up")
])
vote.down.click([
  page.js.alert("down")
])

page.studio.carousel([
  "Great results",
  "Amazing Stuff"
])

filp = page.studio.wedding.flip("Front Side", "Back Side", height=(100, "px"))
filp.heads.style.css.color = 'red'

page.studio.wedding.phone("+1 (303) 499-7111")

#page.ui.studio.events.flip("Front Side", "Back Side", orientation='h') #, height=("auto", ""))

page.ui.calendars.agenda("Super truc", "THis is a test", "20200801T153000Z", "20200802T163000Z")
page.body.style.css.margin = "0 20%"

data = [
        {"text": 'test 1', "status": 'success', 'time': '9h45'},
        {"text": 'test 2', "status": 'error', 'time': '11h45'},
        {"text": 'test 3', "status": 'error', 'time': '12h45'},
        {"text": 'test 4', "status": 'error', 'time': '13h45'},
        {"text": 'test 5', "status": 'pending', 'time': '22h45'}]


line = page.ui.charts.svg.new(width=(100, '%'), height=(30, 'px'))
size = 7
for i in range(0, 20, 2):
  line.line(10 * i, 0, 10 * (i+1), size, stroke="pink")
  line.line(10 * (i+1), size, 10 * (i+2), 0, stroke="pink")

svg = page.studio.news.stepper(data)
svg.html_objs[0].click([
  page.js.alert("dcrevr")
])

imgs_path = "https://colorlib.com/preview/theme/photographer/img/portfolio"
v = "https://process.filestackapi.com/AR8R7qULjSKCgBVrWM8Lwz/resize=width:1110/https://d1elp10n0jayyf.cloudfront.net/u/j-rlxo4lbu.jpg"

page.studio.wedding.avatar(image=v)

page.studio.gallery.mosaic(
  ["%s/%s.jpg" % (imgs_path, i) for i in range(1, 20)]
)

page.studio.wedding.search(options={"lang": 'fr'})
com = page.studio.wedding.comment(avatar=v)
button = page.studio.wedding.button("Comment")
button.click([
  page.js.alert(com.text.dom.content)
])

page.studio.sponsors(logos=["20-MIN.png"])
page.studio.clients(logos=["20-MIN.png"])

page.studio.wedding.background("https://www.brides.com/thmb/2YJma7i3SaWO5COuJLA5x5yEfto=/600x600/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/__opt__aboutcom__coeus__resources__content_migration__brides__public__brides-services__production__2017__06__23__594d1a44c965ef7e40ff23dd_17-ElizaMorrillPhotographyMonseesWedding-90-c7c3e06390db4fb09463a3a02217d407.jpg")

page.studio.locked(
page.studio.wedding.banner("test")
, 1, 8, 2020, 16, 39)

page.studio.wedding.button("test")
#a = page.ui.studio.wedding.address("test")

block = page.studio.wedding.block('''
Use that access code your platform provides—or upgrade to a custom password that will be easier for guests to remember—to make sure that only your invited guests see the details.
''', options={"initial-letter": 35})
#block.text.style.font_family = "Meddon"

title = page.studio.wedding.title("This is a title")
title.style.font_family = "Concert One"

groups = page.ui.div()
for i in range(4):
  groups.add(page.ui.pictos.people())

label = page.ui.div(align="center")
label.add(page.ui.text("This is a test"))
label.add(t)
label.add(page.studio.wedding.delimiter(3))
label.add(page.ui.text("This is a test"))

page.studio.wedding.picture(
  "https://www.brides.com/thmb/VRedUxq8o1V5hKUtXwvglQQu6M0=/600x600/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/i_jvl4-M-a9bb71fe50b24ce79a00158699e5edbb.jpeg",
  label=label
)

page.studio.wedding.time('2020-07-28 20:30:27.243860')


page.studio.wedding.ring()
page.studio.wedding.dress()