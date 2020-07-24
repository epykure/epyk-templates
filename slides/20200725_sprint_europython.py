
from epyk.core.Page import Report

page = Report()

page.body.style.globals.size = 18

slides = page.ui.vignets.slides(start=0)

slides.style.css.display = "block"

slides.add_slide("Epyk - A web Studio library", [
  page.ui.title('''
A centralise library for linking   
'''),
  page.ui.img("epyklogo_whole_big.png?raw=true", path="https://github.com/epykure/epyk-ui/blob/master/epyk/static/images/", width=(300, 'px'))
])

slides.add_slide("Epyk - Architecture", [

  page.ui.img("architecture.PNG?raw=true", path="https://github.com/epykure/epyk-ui/blob/master/epyk/static/images", width=(500, 'px'))
])