# https://www.mcdonalds.com/gb/en-gb/good-to-know/in-our-restaurants/my-mcdonalds-app.html

from epyk.core.Page import Report#


page = Report()
page.headers.favicon("https://image.flaticon.com/icons/svg/732/732217.svg")
page.headers.title("Epyk (App)")

navbar = page.ui.navbar(logo="https://www.mcdonalds.com/content/dam/uk/nfl/logo/logo-80.png", height=(100, 'px'), options={"status": False})
navbar.style.css.border_bottom = None

url_server = "https://www.mcdonalds.com"

conteot = page.ui.div([])
conteot.add(page.ui.text("Did you know you can order and pay contact-free when you use the My McDonald's app? Choose some of your favourites from our reduced menu and pick-up via Drive-Thru or Take-Away.").css({"margin-bottom": '10px'}))
conteot.add(page.ui.buttons.store("%s/content/dam/uk/nfl/icons/app/google-play-uk.jpg" % url_server, "https://smart.link/40ehgllhk8ufl"))
conteot.add(page.ui.buttons.store("%s/content/dam/uk/nfl/icons/app/app-store-uk.jpg" % url_server, "https://smart.link/40ehgllhk8ufl"))


page.ui.vignets.image(title="My McDonald's app", content=conteot,
  image="%s/content/dam/uk/nfl/promo/desktopnfl/app-promo-homepage.png" % url_server
)

page.ui.banners.title(
  title="We're taking extra steps to help keep you and our teams safe.",
  content="Which means we're open for reduced hours and serving a reduced menu."
)

vignets = [
  {"image": "%s/content/dam/uk/nfl/promo/desktopnfl/fc-onethird-order-wherever-enjoy-whenever-mcdonalds-app.jpg" % url_server,
   'title': 'Order ahead contact-free',
   'content': 'Browse the reduced menu in your own time wherever you are, customise your order and save your favourites so you can order again at the tap of a button. Selected restaurants only.'},
  {"image": '%s/content/dam/uk/nfl/promo/desktopnfl/fc-onethird-ready-when-mcdonalds-app.jpg' % url_server,
   "title": 'Ready when you are',
   'content': "Order and pay for your food in our app and we'll start to prepare it for you as soon as you are close to the restaurant. To collect your meal, make yourself known to one of our team outside the restaurant entrance and they will let you know the you can go inside to collect your order, or, if you're driving, head to a Drive-thru lane."},
  {'image': '%s/content/dam/uk/nfl/promo/desktopnfl/fc-onethird-mccafe-loyalty-mcdonalds-app-v1.jpg' % url_server,
   'title': 'McCafé Loyalty',
   'content': 'Our app also allows you to collect and store your McCafé loyalty points!'}
]

row = []
for v in vignets:
  image = page.ui.vignets.image(title=v["title"], render="col", image=v["image"], content=v["content"], height=(500, 'px'))
  image.style.css.border = "1px solid #d6d6d6"
  row.append(image)

row_vignets = page.ui.row(row, width=(80, "%"), align="center")


page.ui.banners.title(
  title="My McDonald's app FAQ",
  content="Select the topic that you're wondering about, then browse the questions to find the answer."
)

items = page.ui.div()
items.add(page.ui.link("Adding available deals to your order"))
items.add(page.ui.link("Currently not available error messages"))
items.add(page.ui.link("Free coffee - McCafé loyalty stickers and stamp"))
items.add(page.ui.link("Ordering"))

page.ui.panels.sliding([items], "Who to use My McDonald's app")