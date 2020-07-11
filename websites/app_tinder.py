# https://tinder.com/

from epyk.core.Page import Report#

# TODO
# - add changing background
# - add SVG logo


page = Report()


page.headers.favicon("https://tinder.com/favicon.ico")
page.headers.title("Epyk (Tinder)")

navbar = page.ui.navbar(logo="https://www.mcdonalds.com/content/dam/uk/nfl/logo/logo-80.png", height=(100, 'px'), options={"status": False})
navbar.no_background()

# https://tinder.com/static/build/f92140b8942048e4fab4906b48c51db4.webp
bg = page.ui.images.wallpaper("https://tinder.com/static/build/f92140b8942048e4fab4906b48c51db4.webp")
bg.style.css.color = "white"
bg.add(page.ui.texts.absolute("Match. Chat. Date.", size_notch=50))
bg.add(page.ui.texts.absolute("By clicking Sign Up, you agree to our Terms. Learn how we process your data in our Privacy Policy", align="center", size_notch=5, top=(55, "%")))

button = page.ui.buttons.absolute("SIGN UP", size_notch=5, top=(60, "%"))
button.style.css.border_radius = "20px"
button.style.css.padding_top = "10px"
button.style.css.padding_bottom = "10px"
button.style.css.width = "20%"
button.style.css.color = "white"
button.style.css.border_color = "white"

button.style.css.background_color = "rgba(0,0,0,0)"
button.style.hover({"background-color": "#fd5068", "color": 'white'})

bg.add(button)
