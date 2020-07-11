# https://www.blablacar.co.uk/

# TODO
# - Improve NavBar
# - Add SVG icons
# - footer


from epyk.core.Page import Report

page = Report()
page.headers.favicon("https://www.blablacar.co.uk/favicon.ico")

page.ui.navbar(height=(60, "px"))

page.ui.banners.info("Coronavirus: for more information about the current situation, please read our FAQ", background="#EDEDED")

page.ui.images.background(url="https://cdn.blablacar.com/kairos/assets/build/images/home_main_large-cf9833201f6f037587b180f79e147430.jpg", height=(500, "px"))

# url("https://cdn.blablacar.com/kairos/assets/build/images/home_driver_large-1d8ac5fb672573235fc5f46ce0acc37c.jpg")

button_style = {"border-radius": '20px', 'background-color': 'rgb(0, 175, 245)', 'color': 'white'}
title_style = {"width": '90%', 'margin': 'auto', 'font-weight': 800, 'line-height': '1.06', 'font-size': '30px', 'color': 'rgb(5, 71, 82)', 'padding': '24px 0px'}

button = page.ui.button("Offer a ride")
button.css(button_style)

content = page.ui.col([
  page.ui.text("Let's make this your least expensive journey ever.", width=(100, "%")),
  button
])
content.style.css.padding = 0

page.ui.vignets.image("Where do you want to drive to?", content=content,
                      image="https://cdn.blablacar.com/kairos/assets/build/images/home_driver_large-1d8ac5fb672573235fc5f46ce0acc37c.jpg")

page.ui.titles.title("Go literally anywhere. From anywhere.").css(title_style)

categories = {
  'Smart': "With access to millions of journeys, you can quickly find people nearby travelling your way.",
  'Simple': "Enter your exact address to find the perfect ride. Choose who you'd like to travel with. And book!",
  'Seamless': "Get to your exact destination, without the hassle. No queues. No waiting around.",
}

row = []
for k, v in categories.items():
  row.append(page.ui.vignets.vignet(title=k, content=v))
page.ui.row(row, align="center", position="top")

page.ui.titles.title("3 things you'll love about BlaBlaCar").css(title_style)

v1 = page.ui.vignets.vignet(title="Smart dashboards", icon="fas fa-tv",
                       content="Combine multiple views of data to get richer insight. Best practices of data visualisation are baked right in.")


v2 = page.ui.vignets.vignet(title="Community", icon="fas fa-tv",
                       content="We take the time to get to know our members. All profiles and ratings are checked. IDs are properly verified. So you know who you're travelling with.")

v3 = page.ui.vignets.vignet(title="Get going faster", icon="fas fa-tv",
                       content="No need to trek across town, catch a ride leaving near you.")


page.ui.row([v1, v2, v3], align="center", position="top")

button = page.ui.button("Discover the BlaBlaBus experience")
button.css(button_style)
content = page.ui.col([
  page.ui.text("Every week, every month. To meet with a loved one, or to discover a new place. With a big family, or a big luggage. To Paris, Amsterdam or any other European destination.", width=(100, "%")),
  button
])
content.style.css.padding = 0

page.ui.vignets.image("Our buses take you to more than 300 cities for small prices.", content=content,
                      image="https://cdn.blablacar.com/kairos/assets/build/images/blablabus4_large-4a66d9018c89e5945b4354e198e7e0c8.jpg")
