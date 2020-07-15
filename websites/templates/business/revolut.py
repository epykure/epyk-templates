# https://www.revolut.com/?p=branded_campaign&ext=VIK_campaign&gclid=EAIaIQobChMIkpG3kpfF6gIVFODtCh26YAV8EAAYASAAEgIrRfD_BwE&_branch_match_id=810280700521664111


from epyk.core.Page import Report
from epyk.core.css.themes import ThemeBlue

from websites.material import revolut_data

page = Report()
page.theme = ThemeBlue.LightBlue()

page.headers.favicon(revolut_data.FAVICON)
page.headers.title(revolut_data.TITLE)
nav = page.ui.navbar(logo=page.ui.text(revolut_data.NAME), height=(60, "px"))
nav.style.css.position = "block"

page.ui.vignets.image(revolut_data.VIGNET_1['title'], content=revolut_data.VIGNET_1['content'], image=revolut_data.VIGNET_1['image'])

page.ui.vignets.image(revolut_data.VIGNET_2['title'], content=page.ui.lists.icons(revolut_data.VIGNET_2['items']),
                      image=revolut_data.VIGNET_2['image'])

page.ui.vignets.image(revolut_data.VIGNET_3['title'], content=page.ui.lists.icons(revolut_data.VIGNET_3['items']),
                      image=revolut_data.VIGNET_3['image'])


page.ui.vignets.image(revolut_data.VIGNET_4['title'], content=page.ui.lists.icons(revolut_data.VIGNET_4['items']),
                      image=revolut_data.VIGNET_4['image'])


page.ui.div([
  page.ui.link("Learn more about Security"),
  #page.ui.pictos.arrow(),
  page.ui.pictos.gout(),
])


page.ui.vignets.price(revolut_data.PRICE_1['value'], revolut_data.PRICE_1['title'], revolut_data.PRICE_1['items'],
                      currency=revolut_data.PRICE_1['currency'])

page.ui.img(revolut_data.IMG_WORLD, path=revolut_data.IMG_STATIC_PATH)

