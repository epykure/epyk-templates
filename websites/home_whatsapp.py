
from epyk.core.Page import Report

page = Report()
page.headers.dev("https://static.whatsapp.net/rsrc.php/v3/yP/r/rYZqPCBaG70.png")
page.headers.title("Whatsapp (Epyk)")

nav = page.ui.navbar(logo="https://static.whatsapp.net/rsrc.php/yv/r/-r3j-x8ZnM7.svg", height=(60, 'px'), options={"status": False})
nav.style.css.background = "#1ebea5"
titles = ["Whatapp Web", "Features"]
for section in titles:
  nav.add(section)
  nav[-1].style.css.color = "white"
  nav[-1].style.css.font_size = "17px"
  nav[-1].style.css.font_weight = 500
  nav[-1].style.css.margin_left = '20px'
  nav[-1].style.css.text_overflow = "ellipsis"

text1 = page.ui.rich.adv_text("TEXTS 2", "Simple, Reliable Messaging",
  '''Message your friends and family for free*. 
WhatsApp uses your phone's Internet connection to send messages so you can avoid SMS fees.''', background="#faf7eb")


text2 = page.ui.rich.adv_text(
  "GROUP CHAT",
  "Groups to keep in touch",
  '''
Keep in touch with the groups of people that matter the most, like your family or coworkers. 
With group chats, you can share messages, photos, and videos with up to 256 people at once. 
You can also name your group, mute or customize notifications, and more.
''', background="#d0e9ea")

container = page.ui.div()
div = page.ui.div(height=(500, "px"), width=(300, "px"))
div.style.css.background_url("https://static.whatsapp.net/rsrc.php/v3/yU/r/aIUMc-wmaFw.png")

container.add(div)
#container.style.css.border = "10px solid white"
container.style.css.text_align = "center"
container.style.css.background = "#faf7eb"


container2 = page.ui.div()
div2 = page.ui.div(height=(500, "px"), width=(300, "px"))
div2.style.css.background_url("https://static.whatsapp.net/rsrc.php/v3/yi/r/faBp1N-tAZL.png")
container2.style.css.background = "#d0e9ea"
container2.add(div2)
#container.style.css.border = "10px solid white"
container2.style.css.text_align = "center"

row = page.ui.row([
  page.ui.col([text1, container], position="top"),
  page.ui.col([text2, container2])
])

row.options.noGutters = True