# https://www.w3schools.com/w3css/tryw3css_templates_coming_soon.ht

from epyk.core.Page import Report#


page = Report()
page.headers.favicon("https://www.google.com/favicon.ico")

bg = page.ui.images.wallpaper("https://wallpapercave.com/wp/wp3188042.jpg")

# Add the company logo
page.ui.images.logo("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png")

# Add the content
title = page.ui.texts.absolute("coming soon", size_notch=52, top=(50, "%"), left=(50, "%"))
time = page.ui.texts.absolute("35 days left", size_notch=12, top=(60, "%"), left=(50, "%"))
title.style.css.text_weight = 5000

#
hr = page.ui.layouts.hr(width=(40, "%"))
hr.style.css.margin = "auto"
hr.style.css.absolute(top=(55, "%"), left=(50, "%"))

bg.add(title)
bg.add(hr)
bg.add(time)
bg.style.color = "white"


content = page.ui.texts.absolute("An excellent search engine", size_notch=12, bottom=(10, "px"), left=(10, "px"))

bg.add(content)