# https://www.paypal.com/uk/home

from epyk.core.Page import Report

from websites.material import blablacar_data
from websites.material import tableau_data


page = Report()
page.headers.favicon("https://c1-odc-15.cdn.office.net/start/s/161311641000_resources/favicon_ppt.ico")

page.body.style.globals.size = 18

slides = page.ui.vignets.slides(start=1)
#slides.title.style.css.color = "green"
#slides.title.style.css.font_size = "35px"

slides.style.css.display = "block"
# slides.style.css.background = "green"

slides.add_slide("Ok", [
  page.ui.title("Page 1")
])
slides[-1].style.css.background = 'white'

button_style = {"border-radius": '20px', 'background-color': 'rgb(0, 175, 245)', 'color': 'white', 'padding': '8px 25px', 'font-size': '18px'}
button = page.ui.button(blablacar_data.BUTTON_DISCOVER, align="center")
button.css(button_style)
button.style.css.margin_top = 10
text_vignet = page.ui.text(blablacar_data.TEXT_DISCOVERY, width=(100, "%"))
text_vignet.style.css.display = False

button.click([text_vignet.dom.show()])
content = page.ui.col([text_vignet, button])
content.style.css.padding = 0

slides.add_slide("Youpi", [
  page.ui.vignets.image(blablacar_data.VIGNET_6['title'], content=content, image=blablacar_data.VIGNET_6['image'])

])

slides[-1].style.css.background = 'white'


rows, row = [], []
for ct in tableau_data.CONTENT:
  row.append(page.ui.vignets.vignet(title=ct["title"], icon=ct["icon"], content=ct["content"], render="row", width=(100, "%")))
  if len(row) == 2:
    rows.append(row)
    row = []
if row:
  rows.append(row)

grid = page.ui.grid(rows, width=(80, "%"))

slides.add([
  grid
])

slides[-1].style.css.background = 'white'

slides.next.click([
  page.js.console.log(slides.dom.content),
  slides.build('''
## Title

### Ok

This is  
''')
])