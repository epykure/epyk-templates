# https://www.uber.com/gb/en/


from epyk.core.Page import Report

page = Report()
page.headers.favicon("https://www.uber.com//favicon.ico")

text = page.ui.text("Uber")
text.style.color = "white"

nav = page.ui.navbar(logo=text, height=(60, "px"))
nav.style.css.background = 'black'
nav.style.padding_left = 20
nav.style.padding_right = 20
# https://www.uber-assets.com/image/upload/v1557179373/assets/1e/106eb3-58af-445d-98dd-41403530fd36/original/modalities_3x2.jpg

page.ui.banners.title(
  "Coronavirus (COVID-19) resources and updates",
  "The safety and well-being of everyone who uses Uber is always our priority. We are actively monitoring the coronavirus (COVID-19) situation and taking steps to help keep our communities safe. Click here for more information.",
  align="left", background="#EDEDED", options={"title_notch": 8, 'title_color': '#1E54B7'})

page.ui.titles.title("Setting 900+ cities in motion")
page.ui.text("View all cities")

bg = page.ui.images.background(url="https://www.uber-assets.com/image/upload/v1557179373/assets/1e/106eb3-58af-445d-98dd-41403530fd36/original/modalities_3x2.jpg", height=(400, "px"))


page.ui.titles.title("Uber for Business")
page.ui.text("The power of Uber in everyday business")

# https://www.uber-assets.com/image/upload/f_auto,q_auto:eco,c_fill,w_1011,h_674/v1585954525/assets/14/fcb55f-8d2c-4037-be40-96265930413e/original/business-eater-horz2x.png
# https://www.uber-assets.com/image/upload/q_auto:eco,c_fill,w_72,h_72/v1542254244/assets/eb/68c631-5041-4eeb-9114-80048a326782/original/document-outlined.svg

bg = page.ui.images.background(url="https://www.uber-assets.com/image/upload/q_auto:eco,c_fill,w_2130,h_1420/v1558736931/assets/e5/fb1f43-f1bf-4dd2-b62d-6015c758d2ee/original/Safety_ilo.svg", size="contain", height=(250, "px"))