# https://www.w3schools.com/w3css/tryw3css_templates_wedding.htm
# https://www.theknot.com/gs/wedding-websites

# TODO
# - List items
# - Images carrousel
# = manage accents
# - banner
# - nav bar

from epyk.core.Page import Report#

page = Report()
page.headers.favicon("https://www.theknot.com/patterns/images/favicon.png")
page.headers.title("Epyk (theknot)")

the_knot = page.ui.text("The knot")
nav = page.ui.navbar(logo=the_knot)
nav.style.css.border_bottom = None
nav.style.css.position = "None"

button_style = {"font-size": '16px', "background": "#e96150", 'border': "1px solid #e96150", 'color': "white", 'padding-top': "6px",
                "padding-bottom": "6px", 'margin-top': "10px"}
margin = "30px"

bg = page.ui.images.background("https://media-api.xogrp.com/images/modern-dash/1674f101-726a-4597-a0a8-3fe3edd60401", height=(500, 'px'))
bg.style.css.color = "white"

slogan = page.ui.text("The Knot Wedding Website", width=(60, "%"))
slogan.style.css.font_size = "50px"
slogan.style.css.display = "inline-block"
slogan.style.css.margin_top = 60
bg.add(slogan)

content = page.ui.text("Share wedding details, collect RSVPs and sync your registry all in one place.", width=(60, "%"))
content.style.css.display = "inline-block"
content.style.css.font_size = "20px"
bg.add(content)

button = page.ui.button("Start now", width=(150, 'px')).css(button_style)
button.style.css.margin_left = "20%"
bg.add(button)


members = page.ui.text("Already a member? Log In", width=(60, "%"))
members.style.css.display = "inline-block"
members.style.css.font_size = "20px"
bg.add(members)

boxes = [
  {"title": 'Designs That Match Your Style', 'content': 'Choose from tons of designs and customize your Wedding Website to be unapologetically you.'},
  {"title": 'Do It Your Way', 'content': 'Make it uniquely you with a personalized URL, custom cover photo and unique color scheme.'},
  {"title": 'Guests Just Get It', 'content': 'Yep, even grandma. Our Wedding Website templates make getting all the info super simple.'},
]

row = []
for rec in boxes:
  row.append(page.ui.col([
    page.ui.titles.title(rec['title']).css({"text-align": 'center'}),
    page.ui.text(rec['content'], align="center")], align="center"))
page.ui.row(row, width=(90, '%'), align="center").css({"margin-top": margin, "margin-bottom": margin})

page.ui.banners.title(
  title="New Wedding Website Templates That Feel Like You",
  content="Customizable background photos, color options galore you. do. you. Not loving the look? Swap it out (for free!) whenever you want.",
  background="#f5f6f8"
).css({"margin-top": margin, "margin-bottom": margin})

b2 = page.ui.button("See All Designs", align="center").css(button_style)


page.ui.vignets.image(
  title="The Easiest Set-Up Ever",
  content="Because syncing your registries and personalizing a free wedding website seriously should be this simple.",
  image="https://media-api.xogrp.com/images/929612c1-78e5-43d4-ab9e-528f9b24d276~rs_560.h"
).css({"margin-top": margin, "margin-bottom": margin})

page.ui.vignets.image(
  title="Convenient for Everyone",
  content="You have a lot going on. So do guests. That’s why we created a single place for RSVPs, meals, hotel rooms and all your other wedding info to live.",
  image="https://media-api.xogrp.com/images/e9f03fe3-1b83-4b0c-9fca-3b5b50cf8be6~rs_560.h",
  options={"picture": 'right'}
).css({"margin-top": margin, "margin-bottom": margin})

page.ui.vignets.image(
  title="Invites That Actually Match",
  content="#Twinning is still a thing when it comes to invites and a free Wedding Website. Check out a few from Minted, Wedding Paper Divas and more that complement your style.",
  image="https://media-api.xogrp.com/images/9054afac-fc4b-4706-9196-fc865c0bb1ba~rs_560.h",
).css({"margin-top": margin, "margin-bottom": margin})


page.ui.banners.title(
  title="The Knot Wedding Website 101",
  content="Not sure where to start? We've got you. Check out these essential articles that go over the ins, the outs and everything else you need to know about weddings.",
  background="#f5f6f8")

vignets = [
  {"image": "https://media-api.xogrp.com/images/248e54f0-b54a-4b09-b4d2-2d303b6d260e~rs_660.h",
   'title': 'You Might Want to Include These on Your Website'},
  {"image": 'https://media-api.xogrp.com/images/16fbed86-15c8-42ac-9a24-5dedd1e46b0a~rs_660.h',
   "title": "What the Best Wedding Websites Do (and Don't Do)"},
  {'image': 'https://media-api.xogrp.com/images/ac884345-7340-4220-9c1e-6ef6951985bb~rs_330.h',
   'title': 'Most-Loved Tools for Free Wedding Websites'}
]

row = []
for v in vignets:
  image = page.ui.vignets.image(title=v["title"], render="col", image=v["image"], height=(500, 'px'))
  image.style.css.border = "1px solid #d6d6d6"
  row.append(image)
row_vignets = page.ui.row(row, width=(80, "%"), align="center")
row_vignets.style.css.background = "#f5f6f8"
row_vignets.css({"margin-top": margin, "margin-bottom": margin})

page.ui.banners.title(
  title="Got Questions About The Knot Wedding Website?",
  content="We can help! Get answers ASAP with our FAQs below or shoot our customer service team a note anytime at help@theknot.com.")


page.ui.banners.title(
  title="Wedding Planning Has Never Been Easier",
  content="Sign up for The Knot and get access to your all-in-one wedding planner.")

contents = [
  {"title": 'Wedding Vision', 'icon': 'far fa-lightbulb', 'content': 'Define your wedding style and get matched with local vendors.'},
  {"title": 'Wedding Websites', 'icon': 'fas fa-user-friends', 'content': 'Create your free custom website to share with family and friends.'},
  {"title": 'Budgeter', 'icon': 'fas fa-globe-europe', 'content': 'Get a personalized spending plan based on your unique budget.'},
  {"title": 'Checklist', 'icon': 'fas fa-tv', 'content': 'Always know what to do, when, with your 24/7 wedding planner.'},

  {"title": 'Guest List', 'icon': 'fas fa-wrench', 'content': 'Gather addresses, collect RSVPs, track thank-you notes and more.'},
  {"title": 'Vendor List', 'icon': 'fas fa-comments', 'content': 'Streamline your vendor contacts and get pro recommendations.'},
  {"title": 'Registry', 'icon': 'fas fa-comments', 'content': 'Your retail, cash, experience and charity registries, all in one place.'},
  {"title": 'Wedding Day Timeline', 'icon': 'fas fa-comments', 'content': 'The who, what, when and where of your wedding day in one timeline.'},

]

rows, row = [], []
for ct in contents:
  row.append(page.ui.vignets.vignet(title=ct["title"], icon=ct["icon"], content=ct["content"], render="col", width=(100, "%")))
  if len(row) == 4:
    rows.append(row)
    row = []
if row:
  rows.append(row)
grid = page.ui.grid(rows, width=(80, "%"))

page.ui.banners.title(
  title="The Best Things in Life Are Free",
  content="Like our Wedding Website templates for example."
)

b2 = page.ui.button("Personalize Yours", align="center").css(button_style)

page.ui.banners.text('''
Thanks to our photographers: “Kaela & Isiah” photo by Carolyn Scott Photography; “Lila & Kham” photo by Jana Williams Photography; “Chaz & Grant” photo by Sincerely, Emelia; “Eileen & Johnny” photo by Perpixel Photography; “Lisa & Tim” photo by T & S Hughes Photography; “Laura & Leah” photo by Amanda Wei Photography; “Tuyet & Raephael” photo by Heather Bode; “Cherie & Joe” photo by Alison Conklin Photography; Shutterstock; Christin Hume on Unsplash; Featured Invitation: Minted/Gilt Agate by Kaydi Bishop
''', width=(80, "%"), size_notch=-2)