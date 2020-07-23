# https://www.julianabicycles.com/en-US


from epyk.core.Page import Report
from websites.material import julianabicycles_data


page = Report()
page.headers.favicon(julianabicycles_data.FAVICON)

carrousel = page.ui.images.carrousel(julianabicycles_data.IMAGES, path=julianabicycles_data.IMG_PATH)


page.ui.images.animated(julianabicycles_data.IMAGES[0], path=julianabicycles_data.IMG_PATH)

banner = page.ui.banners.text(
  page.ui.row([
    page.ui.col([
      page.ui.subtitle("Title"),
      page.ui.link("HTML Tutorial")
    ]),
    page.ui.col([
      page.ui.subtitle("Social"),
      page.ui.div([
        page.ui.icons.twitter(),
        page.ui.icons.facebook(),
      ])
    ])
  ])
)

carrousel.touch.swap(
  [page.js.alert("left")],
  [page.js.alert("right")]
)

page.ui.banners.disclaimer(links=[{"text": "Cookies, Terms % Privacy"}, 'About', 'Contact us'])