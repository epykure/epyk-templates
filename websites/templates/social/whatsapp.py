
from epyk.core.Page import Report
from websites.material import whatsapp_data


page = Report()
page.headers.dev(whatsapp_data.FAVICON)
page.headers.title(whatsapp_data.TITLE)

nav = page.ui.navbar(logo=whatsapp_data.LOGO, height=(60, 'px'))
nav.style.css.background = "#1ebea5"

for section in whatsapp_data.TITLES:
  nav.add(section)
  nav[-1].style.css.color = "white"
  nav[-1].style.css.font_size = "17px"
  nav[-1].style.css.font_weight = 500
  nav[-1].style.css.margin_left = '20px'
  nav[-1].style.css.text_overflow = "ellipsis"

text1 = page.ui.rich.adv_text(whatsapp_data.TEXT_ADV['section'], whatsapp_data.TEXT_ADV['title'], whatsapp_data.TEXT_ADV['content'], background="#faf7eb")
text2 = page.ui.rich.adv_text(whatsapp_data.TEXT_ADV_2['section'], whatsapp_data.TEXT_ADV_2['title'], whatsapp_data.TEXT_ADV_2['content'], background="#d0e9ea")

container = page.ui.div()
div = page.ui.div(height=(500, "px"), width=(300, "px"))
div.style.css.background_url(whatsapp_data.BACKGROUND_1)

container.add(div)
container.style.css.text_align = "center"
container.style.css.background = "#faf7eb"

container2 = page.ui.div()
div2 = page.ui.div(height=(500, "px"), width=(300, "px"))
div2.style.css.background_url(whatsapp_data.BACKGROUND_2)
container2.style.css.background = "#d0e9ea"
container2.add(div2)
container2.style.css.text_align = "center"

row = page.ui.row([page.ui.col([text1, container], position="top"), page.ui.col([text2, container2])])
row.options.noGutters = True
