# https://www.tableau.com/en-gb/trial/tableau-software


from epyk.core.Page import Report
from websites.material import tableau_data


page = Report()
page.headers.dev(tableau_data.FAVICON)
button_css = {"border-radius": '20px', "border": '1px solid #ff6d02', 'color': '#ff6d02', 'margin-bottom': '20px'}

logo = page.ui.div(height=(30, "px"), width=(30, "px"))
logo.style.css.background_url(tableau_data.LOGO, size="auto 30px")
logo.style.css.display = "inline-block"
logo.style.css.margin_top = "-10px"
logo.style.css.margin_right = "10px"

company = page.ui.text(tableau_data.LOGO_NAME)
company.style.css.font_size = "17px"
company.style.css.font_weight = 800
company.style.css.text_transform = 'uppercase'
company.style.css.letter_spacing = '2px'

nav = page.ui.navbar(logo=page.ui.div([logo, company]), height=(80, "px"))
nav.style.css.padding_left = "30px"
nav.style.css.position = "None"

bg = page.ui.images.background(tableau_data.BACKGROUND_IMAGE, height=(360, "px"), position="middle")
bg.style.css.color = "white"

slogan = page.ui.text(tableau_data.SLOGAN, align="center", width=(60, "%"))
slogan.style.css.font_size = "50px"
slogan.style.css.display = "inline-block"
slogan.style.css.margin_top = 60
bg.add(slogan)

try_tableau = page.ui.button(tableau_data.BUTTON_TRY)
try_tableau.css(button_css).css({'color': 'white', 'background': '#ff6d02', 'font-size': '15px', 'margin-right': '20px'})

see_tablea = page.ui.button(tableau_data.BUTTON_SEE)
see_tablea.no_background()
see_tablea.css(button_css).css({'color': 'white', "border": '1px solid white', 'font-size': '15px'})

bg.add(page.ui.div([try_tableau, see_tablea]).css({"text-align": 'center'}))
bg.add(page.ui.text(tableau_data.TEXT_TRIAL_VERSION))

banner = page.ui.banners.text(tableau_data.BANNER_TEXT, size_notch=25, align="center")
banner.style.css.width = "80%"

rows, row = [], []
for ct in tableau_data.CONTENT:
  row.append(page.ui.vignets.vignet(title=ct["title"], icon=ct["icon"], content=ct["content"], render="row", width=(100, "%")))
  if len(row) == 2:
    rows.append(row)
    row = []
if row:
  rows.append(row)

grid = page.ui.grid(rows, width=(80, "%"))
grid.style.css.margin_bottom = 40

try_button = page.ui.button(tableau_data.BUTTON_TRY.upper(), align="center")
try_button.css(button_css)
try_button.no_background()

link = page.ui.link(tableau_data.TABLEAU_SPEC, url="#specTech", htmlCode="specTech")
link.style.css.color = "orange"

specs = page.ui.div("test")
specs.style.css.display = False

link.click([specs.dom.toggle()])
col = page.ui.col([try_button, page.ui.text("FULL VERSION TRIAL NO CREDIT CARD REQUIRED", align="center"), link, specs])

banner = page.ui.banners.text(col, background="#fafafa")

row = [page.ui.vignets.image(title=v["title"], render="col", image=v["image"], content=v["content"]) for v in tableau_data.VIGNETS]
row_vignets = page.ui.row(row, width=(80, "%"), align="center")

quote = page.ui.banners.quote(tableau_data.QUOTE, size_notch=15, author="RAPHAEL STEIN", background="#464646")
quote.style.css.color = "#bbb"
quote.style.css.padding = "40px 10%"
quote.style.css.margin = "40px 0"

about_tableau = page.ui.banners.title(tableau_data.BANNER_ABOUT['title'], tableau_data.BANNER_ABOUT['content'])
about_tableau.style.css.padding = "40px 10%"

footer = page.ui.banners.text("", background="black")
