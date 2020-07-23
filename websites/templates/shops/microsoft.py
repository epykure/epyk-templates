# https://www.microsoft.com/en-gb/


from epyk.core.Page import Report
from websites.material import microsoft_data


page = Report()
page.headers.favicon(microsoft_data.FAVICON)
page.headers.title("Epyk (Microsoft)")

nav = page.ui.navbar(logo="%s%s" % (microsoft_data.ITEM_PATH, microsoft_data.LOGO), height=(30, "px"))
nav.style.css.padding_left = "30px"
nav.style.css.position = "None"

row = []
for item in microsoft_data.ITEMS:
  row.append(page.ui.col([
    page.ui.img(item['img'], path=microsoft_data.ITEM_PATH, width=(40, "px")),
    page.ui.text(item['text'], align="center")
  ]))

row = page.ui.row(row)
row.style.css.margin = "20px auto"

image = page.ui.images.background("%s%s" % (microsoft_data.ITEM_PATH, microsoft_data.XBOX), height=(500, "px"))

page.ui.title("For Work")

page.ui.vignets.background("%s%s" % (microsoft_data.ITEM_PATH, microsoft_data.REMOTE))

page.ui.banners.follow("Follow Microsoft", width=(90, "%"))

page.ui.banners.row(microsoft_data.ROW_HEADERS, microsoft_data.ROW_LINKS)

page.ui.banners.disclaimer(microsoft_data.DISCLAIMER_TEXT, links=microsoft_data.DISCLAIMER_LINKS)
