
import config

from epyk.core.Page import Report
from epyk.core.css.themes import ThemeDark

# Create a basic report object
rptObj = Report()

#
rptObj.theme = ThemeDark.Dark()
rptObj.theme.colors[-1] = "yellow"


rptObj.ui.images.circular("epykIcon.PNG", path=config.IMG_PATH)

rptObj.ui.layouts.new_line()
rptObj.ui.images.avatar("Epyk", status='out')
rptObj.ui.images.avatar(image="epykIcon.PNG", path=config.IMG_PATH, status=False)

rptObj.ui.layouts.new_line()
rptObj.ui.images.badge("Test badge", "Label", icon="fas fa-align-center")
rptObj.ui.images.badge("This is a badge", background_color="red", color="white")
rptObj.ui.images.badge(12, icon="far fa-bell", options={"badge_position": 'left'})


car = rptObj.ui.images.carrousel(["epykIcon.PNG", "epyklogo.ico", "epyklogo_whole_big.png"],
                                 path=config.IMG_PATH, height=(200, 'px'))
car.click([rptObj.js.console.log('data', skip_data_convert=True)])

#
c1 = rptObj.ui.images.badge(3, icon="far fa-bell", url="test")
c1.style.display = None
rptObj.ui.layouts.div([c1], align='right')
rptObj.ui.button("display").click(c1.dom.toggle())

# from epyk.core.html import Defaults
#
# Defaults.SERVER_PATH = r"C:\Pictures"
# rptObj.ui.images.animated("philo.PNG")

rptObj.ui.images.emoji(rptObj.symbols.smileys.DISAPPOINTED_FACE)
#
# rptObj.ui.button("test")
#
# a = rptObj.ui.images.animated("epykIcon.PNG", text="This is a comment", title="Title", url="#", path=r"../../../static/images")
# a.style.css.borders()
#
# b = rptObj.ui.images.animated("epykIcon.PNG", text="This is a comment", title="Title", url="#", path=r"../../../static/images")
# b.style.css.borders()
#
# c = rptObj.ui.images.animated("epykIcon.PNG", text="This is a comment", title="Title", url="#", path=r"../../../static/images")
# c.style.css.borders()
#
# rptObj.ui.layouts.row([a, b, c])
#
# rptObj.ui.button("test").click([
#   c.title.build("ok"),
#   c.text.build("this is a test")
# ])

t = rptObj.ui.text("Test")
t.style.font_size = 20
t.style.effects.translate(1)


rptObj.ui.icons.epyk()

#rptObj.style.imports("toto")
print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_image"))
