
from epyk_studio.core.Page import Report
from PIL import Image

import os

page = Report()
page.headers.dev()

path = r"C:\tests"

epyk_logo = "https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epyklogo.ico"
path = r""

html_impage = page.ui.img(epyk_logo)

img = Image.open(os.path.join(path, "epyklogo.ico"))
px = img.load()

colors = set()
for i in range(img.size[0]): # for every pixel:
  for j in range(img.size[1]):
    r, g, b = px[i, j][:3]
    #if max(*px[i, j]) == px[i, j][-1] and r+g - b < 0.9*b and b > 20:
    #  px[i, j] = (255, 0, 0)
    colors.add(px[i, j])

d = page.ui.div()
for c in sorted(colors):
  d.add(page.ui.rich.color(c))

page.ui.title("Image and colors")
page.ui.row([html_impage, d])
