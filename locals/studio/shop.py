
from epyk.core.Page import Report#


page = Report()
page.headers.dev()

p1 = page.ui.studio.shop.product( '''
ASUS PC portable Gamer FX571GT-BQ691T 15" FHD - Core i5-8300H - RAM 8Go - Stockage 512Go SSD - GTX 1650 4Go - Windows 10
''', 699.99, 'https://www.cdiscount.com/pdt2/9/1/t/1/300x300/fx571gtbq691t/rw/asus-pc-portable-gamer-fx571gt-bq691t-15-fhd-co.jpg', 4)
p1.image.style.css.height = "140px"
p1.image.style.css.width = "140px"

p2 = page.ui.studio.shop.product( '''
Tablette Tactile - SAMSUNG Galaxy Tab A - 10,1" - RAM 2Go - Android 9.0 - Stockage 32Go - WiFi - Noir0
''', 199.99, 'https://www.cdiscount.com/pdt2/x/e/f/1/300x300/smt510nzkdxef/rw/tablette-tactile-samsung-galaxy-tab-a-10-1.jpg', 4)
# product
p2.image.style.css.height = "140px"
p2.image.style.css.width = "140px"

p3 = page.ui.studio.shop.product( '''
Imprimante multifonctionHP Color LaserJet Pro M182n
''', 199.99, 'https://www.cdiscount.com/pdt2/9/4/2/1/300x300/auc0193905484942/rw/imprimante-multifonctionhp-color-laserjet-pro-m182.jpg', 4)
# product
p3.image.style.css.height = "140px"
p3.image.style.css.width = "140px"

page.ui.row([p1, p2, p3])

page.ui.layouts.hr()

page.ui.studio.shop.price_from(1889.54)

page.ui.studio.shop.availability(False, "Only 2 left in stock.")