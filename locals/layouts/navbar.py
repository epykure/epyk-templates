

from epyk.core.Page import Report


page = Report()
page.headers.dev()

nav_bar = page.ui.navigation.bar(title="This is a title")
nav_bar.add(page.ui.buttons.small("Test", icon="fab fa-js").css({"margin": '0 5px'}))
nav_bar.add(page.ui.link("link"))

page.ui.text("This is a text")
page.ui.layouts.br(50)
