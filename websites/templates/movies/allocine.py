# http://www.allocine.fr/


from epyk.core.Page import Report#
from websites.material import allocine_data


page = Report()
page.headers.favicon(allocine_data.FAVICON)

navbar = page.ui.navbar(logo=allocine_data.LOGO, height=(40, "px"), options={'logo_height': (20, 'px')})
navbar[0].style.css.width = "200px"
navbar.style.css.background_color = '#fecc00'

page.ui.images.background(allocine_data.CARROUSEL[0], height=(350, "px"), size="contain")

page.ui.title(page.py.encode_html(allocine_data.NEW_CINE)).css({"margin": '20px 1% 0 1%'})

vignets = []
for v in allocine_data.VIGNETS:
  vignets.append(page.ui.vignets.image(title=page.py.encode_html(v['title']), image=v['image'], content=page.py.encode_html(v['content']), render="col"))
row = page.ui.row(vignets)