# https://www.tableau.com/en-gb/trial/tableau-software


from epyk.core.Page import Report

page = Report()
page.headers.dev("https://www.tableau.com/favicon.ico")

button_css = {"border-radius": '20px', "border": '1px solid #ff6d02', 'color': '#ff6d02', 'margin-bottom': '20px'}

logo = page.ui.div(height=(30, "px"), width=(30, "px"))
logo.style.css.background_url("https://cdns.tblsft.com/sites/all/themes/tabwow/logo.png", size="auto 30px")
logo.style.css.display = "inline-block"
logo.style.css.margin_top = "-10px"
logo.style.css.margin_right = "10px"

company = page.ui.text("Tableau")
company.style.css.font_size = "17px"
company.style.css.font_weight = 800
company.style.css.text_transform = 'uppercase'
company.style.css.letter_spacing = '2px'

nav = page.ui.navbar(logo=page.ui.div([logo, company]), height=(80, "px"))
nav.style.css.padding_left = "30px"
nav.style.css.position = "None"

bg = page.ui.images.background("https://cdns.tblsft.com/sites/default/files/hero/1366x455_desktop_hero_4.jpg", height=(360, "px"), position="middle")
bg.style.css.color = "white"

slogan = page.ui.text("We're changing the way you think about data", align="center", width=(60, "%"))
slogan.style.css.font_size = "50px"
slogan.style.css.display = "inline-block"
slogan.style.css.margin_top = 60
bg.add(slogan)

try_tableau = page.ui.button("Try tableau for free")
try_tableau.css(button_css).css({'color': 'white', 'background': '#ff6d02', 'font-size': '15px', 'margin-right': '20px'})

see_tablea = page.ui.button("SEE IN ACTION")
see_tablea.no_background()
see_tablea.css(button_css).css({'color': 'white', "border": '1px solid white', 'font-size': '15px'})

bg.add(page.ui.div([try_tableau, see_tablea]).css({"text-align": 'center'}))
bg.add(page.ui.text("FULL-VERSION TRIAL. NO CREDIT CARD REQUIRED."))


banner = page.ui.banners.text("Tableau is business intelligence software that helps people see and understand their data.", size_notch=25, align="center")
banner.style.css.width = "80%"

contents = [
  {"title": 'Fast analytics', 'icon': 'far fa-lightbulb', 'content': 'Connect and visualise your data in minutes. Tableau is ten to one hundred times faster than existing solutions.'},
  {"title": 'Ease of use', 'icon': 'fas fa-user-friends', 'content': 'Anyone can analyse data with intuitive drag-&-drop products. No programming, just insight.'},
  {"title": 'Big data, any data', 'icon': 'fas fa-globe-europe', 'content': 'From spreadsheets to databases to Hadoop to cloud services, explore any data.'},
  {"title": 'Smart dashboards', 'icon': 'fas fa-tv', 'content': 'Combine multiple views of data to get richer insight. Best practices of data visualisation are baked right in.'},
  {"title": 'Update automatically', 'icon': 'fas fa-wrench', 'content': 'Get the freshest data with a live connection to your data or get automatic updates on a schedule you define.'},
  {"title": 'Share in seconds', 'icon': 'fas fa-comments', 'content': 'Publish a dashboard with a few clicks to share it live on the web and on mobile devices.'},

]

rows, row = [], []
for ct in contents:
  row.append(page.ui.vignets.vignet(title=ct["title"], icon=ct["icon"], content=ct["content"], render="row", width=(100, "%")))
  if len(row) == 2:
    rows.append(row)
    row = []
if row:
  rows.append(row)

grid = page.ui.grid(rows, width=(80, "%"))
grid.style.css.margin_bottom = 40

try_button = page.ui.button("TRY TABLEAU FOR FREE", align="center")
try_button.css(button_css)
try_button.no_background()

link = page.ui.link("+ VIEW TECH SPECS", url="#specTech", htmlCode="specTech")
link.style.css.color = "orange"

specs = page.ui.div("test")
specs.style.css.display = False

link.click([specs.dom.toggle()])

col = page.ui.col([
  try_button,
  page.ui.text("FULL VERSION TRIAL NO CREDIT CARD REQUIRED", align="center"),
  link,
  specs
])

banner = page.ui.banners.text(col, background="#fafafa")

vignets = [
  {"image": "https://cdnl.tblsft.com/sites/default/files/overviewtemplate_20.jpg", 'title': 'CUSTOMER STORY', "content": 'Wells Fargo wrangles data from over 70 million customers to redesign customer banking portal'},
  {"image": "https://cdnl.tblsft.com/sites/default/files/overview/stories/tales_of_100-500x500.png", 'title': 'VISUALISATION', "content": "Test the myth of tech companies' 'rocket-ship' growth"},
  {"image": "https://cdns.tblsft.com/sites/default/files/500x500_desktop_seeitinaction.jpg", 'title': 'PRODUCT VIDEO', "content": "Create rich analyses and share your insights with colleagues in seconds"},
]

row = []
for v in vignets:
  row.append(page.ui.vignets.image(title=v["title"], render="col", image=v["image"], content=v["content"]))

row_vignets = page.ui.row(row, width=(80, "%"), align="center")

value = "When we took the first dashboard done in Tableau to the first meeting with the executives, some were so surprised that the reaction was mostly silence. One of the executives said, 'I always asked for that in the BI area and finally they managed to do it.'"

quote = page.ui.banners.quote(value, size_notch=15, author="RAPHAEL STEIN", background="#464646")
quote.style.css.color = "#bbb"
quote.style.css.padding = "40px 10%"
quote.style.css.margin = "40px 0"


about_tableau = page.ui.banners.title("About Tableau",'''
Tableau helps people transform data into actionable insights. Explore with limitless visual analytics. 
Build dashboards and perform ad hoc analyses in just a few clicks. 
Share your work with anyone and make an impact on your business. 
From global enterprises to early-stage startups and small businesses, people everywhere use Tableau to see and understand their data.
''')

about_tableau.style.css.padding = "40px 10%"

footer = page.ui.banners.text("", background="black")
