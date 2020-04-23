
import config

from epyk.core.Page import Report
from epyk.core.css.themes import ThemeDark

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Change the theme of the report
rptObj.theme = ThemeDark.Dark()

# Change the first color of this theme (overrride)
rptObj.theme.colors[-1] = "yellow"

# Add icon
# The path for the icon is defind in config
rptObj.ui.images.circular("epykIcon.PNG", path=config.IMG_PATH)

rptObj.ui.layouts.new_line()

# Avatar with a status
rptObj.ui.images.avatar("Epyk", status='out')

# Avatar with an image
rptObj.ui.images.avatar(image="epykIcon.PNG", path=config.IMG_PATH, status=False)

# Add badges
rptObj.ui.layouts.new_line()
rptObj.ui.images.badge("Test badge", "Label", icon="fas fa-align-center")

rptObj.ui.layouts.new_line()
rptObj.ui.images.badge("This is a badge", background_color="red", color="white")

rptObj.ui.layouts.new_line()
rptObj.ui.images.badge(12, icon="far fa-bell", options={"badge_position": 'left'})

# Add a carrousel of images
car = rptObj.ui.images.carrousel(["epykIcon.PNG", "epyklogo.ico", "epyklogo_whole_big.png"], path=config.IMG_PATH, height=(200, 'px'))
car.click([rptObj.js.console.log('data', skip_data_convert=True)])

# Add a simple badge
c1 = rptObj.ui.images.badge(3, icon="far fa-bell", url="test")
c1.style.display = None

# Add the badge to a container on the right
rptObj.ui.layouts.div([c1], align='right')
rptObj.ui.button("display").click(c1.dom.toggle())

# Add an emoji
rptObj.ui.images.emoji(rptObj.symbols.smileys.DISAPPOINTED_FACE)

# Add an animated picture
a = rptObj.ui.images.animated("epykIcon.PNG", text="This is a comment", title="Title", url="#", path=config.IMG_PATH)
a.style.css.borders()

# Add multiple badge on the same row
rptObj.ui.images.badge("306", url="google", icon="fas fa-align-center", options={'badge_css': {'color': 'white', "background": 'red'}})
rptObj.ui.images.badge("306", url="google", icon="fas fa-align-center", options={'badge_css': {'color': 'white', "background": 'orange'}})
rptObj.ui.images.badge("306", url="google", icon="fas fa-align-center", options={'badge_css': {'color': 'white', "background": 'red'}})
rptObj.ui.images.badge("306", url="google", icon="fas fa-align-center", options={'badge_css': {'color': 'white', "background": 'red'}})
b = rptObj.ui.images.badge(7688, icon="fab fa-python", options={'badge_css': {'color': 'white', "background": 'red'}})
b.options.badge_css = {"background": 'green'}

i = rptObj.ui.layouts.icons(["fas fa-align-center", 'fab fa-python'])
i.icon.click([i.icon.dom.css({"color": 'red'})])

t = rptObj.ui.text("Test")
t.style.font_size = 20
t.style.effects.translate(1)

# Add the epyk icon
rptObj.ui.icons.epyk()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
