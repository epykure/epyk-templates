
from epyk_studio.core.Page import Report#


page = Report()
page.headers.dev()

page.studio.shop.theme()
page.studio.shop.button("click")


page.studio.shop.album(
  ["https://images-na.ssl-images-amazon.com/images/I/713oawHjRRL._AC_SX679_.jpg",
   {'min': "https://images-na.ssl-images-amazon.com/images/I/51UpndiaCrL._AC_US40_.jpg",
    'max': "https://images-na.ssl-images-amazon.com/images/I/71WFRqN2FnL._AC_SL1500_.jpg"},
   "https://images-na.ssl-images-amazon.com/images/I/51hTX8TDJ%2BL._AC_US40_.jpg",
   "https://images-na.ssl-images-amazon.com/images/I/41zkbUZ2x9L._AC_US40_.jpg"])
# https://images-na.ssl-images-amazon.com/images/I/713oawHjRRL._AC_SX679_.jpg

dsc = page.studio.shop.description('''
ASUS PC portable Gamer FX571GT-BQ691T 15" FHD - Core i5-8300H - RAM 8Go - Stockage 512Go SSD - GTX 1650 4Go - Windows 10
''', 'https://www.amazon.co.uk/Q-Connect-Plain-Flipchart-Sheet-Pack/dp/B000NM4GT6?ref_=Oct_s9_apbd_simh_hd_bw_bDNhzj&pf_rd_r=S8A1HQCEH6YFV3D73V2H&pf_rd_p=f6e3c37a-5b3c-522e-be1a-6d3fc1001d89&pf_rd_s=merchandised-search-11&pf_rd_t=BROWSE&pf_rd_i=197743031',)

page.studio.shop.quality({2: 34, 4: 56}, url="test=%s")
#page.ui.studio.shop.discount(5)
page.studio.shop.price_discount(999.99, 10)
page.studio.shop.question('Hi, mine arrived without a pen. How do I get the pen which should come with it?', url="#")

page.ui.qrcode("https://davidshimjs.github.io/qrcodejs")

page.studio.shop.rating(2, 85, "")

page.studio.shop.order(2)

page.studio.shop.tags(["computing", "game", "laptop"])

p1 = page.studio.shop.product(dsc, 699.99, 'https://www.cdiscount.com/pdt2/9/1/t/1/300x300/fx571gtbq691t/rw/asus-pc-portable-gamer-fx571gt-bq691t-15-fhd-co.jpg', 4)
p1.image.style.css.height = "140px"
p1.image.style.css.width = "140px"

p2 = page.studio.shop.product( '''
Tablette Tactile - SAMSUNG Galaxy Tab A - 10,1" - RAM 2Go - Android 9.0 - Stockage 32Go - WiFi - Noir0
''', 199.99, 'https://www.cdiscount.com/pdt2/x/e/f/1/300x300/smt510nzkdxef/rw/tablette-tactile-samsung-galaxy-tab-a-10-1.jpg', 4)
# product
p2.image.style.css.height = "140px"
p2.image.style.css.width = "140px"

p3 = page.studio.shop.product( '''
Imprimante multifonctionHP Color LaserJet Pro M182n
''', 199.99, 'https://www.cdiscount.com/pdt2/9/4/2/1/300x300/auc0193905484942/rw/imprimante-multifonctionhp-color-laserjet-pro-m182.jpg', 4)
# product
p3.image.style.css.height = "140px"
p3.image.style.css.width = "140px"

page.ui.row([p1, page.studio.shop.label(p2, 'discount'), p3])

page.ui.layouts.hr()

page.studio.shop.price_from(1889.54)

page.studio.shop.availability(False, "Only 2 left in stock.")