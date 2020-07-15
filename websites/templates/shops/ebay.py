# https://www.ebay.com/


from epyk.core.Page import Report
from websites.material import ebay_data


page = Report()
page.headers.favicon(ebay_data.FAVICON)
page.headers.title(ebay_data.TITLE)

nav = page.ui.navbar(logo=ebay_data.LOGO)

page.ui.img(image=ebay_data.IMG_0, path=ebay_data.IMG_PATH)
page.ui.img(image=ebay_data.IMG_1, path=ebay_data.IMG_PATH)
