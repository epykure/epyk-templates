# https://www.tableau.com/en-gb/trial/tableau-software


from epyk.core.Page import Report

page = Report()
page.headers.dev("https://www.tableau.com/favicon.ico")

page.ui.navbar(logo="https://cdns.tblsft.com/sites/all/themes/tabwow/logo.png")

container = page.ui.div()
title = page.ui.titles.title("Smart dashboards", width=("auto", ""))
title.style.css.display = "inline-block"
text = page.ui.text("Combine multiple views of data to get richer insight. Best practices of data visualisation are baked right in.")
text.style.css.display = "block"

# https://cdns.tblsft.com/sites/default/files/hero/1366x455_desktop_hero_4.jpg
col = page.ui.col([
  title, text
])
col.style.css.border_left = "1px solid black"
container.add(page.ui.icons.awesome("fas fa-tv", width=(30, "px"), height=(30, "px")))
container.add(col)

bg = page.ui.images.background("https://cdns.tblsft.com/sites/default/files/hero/1366x455_desktop_hero_4.jpg")
bg.add(page.ui.button("test"))