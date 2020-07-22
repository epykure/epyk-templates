# https://www.python.org/

from epyk.core.Page import Report#
from websites.material import python_data


page = Report()
page.headers.favicon(python_data.FAVICON)

row = []
for _ in range(4):
  col = page.ui.col()
  col.attr["class"].add("mx-1")
  col.set_size(None)
  col.attr["class"].add("col-sm-auto")
  #col.attr["class"].add("offset-sm-3")
  title = page.ui.title("Get Started")
  text = page.ui.text("Whether you're new to programming or an experienced developer, it's easy to learn and use Python.")

  link = page.ui.link(page.py.encode_html("Top ⁁ catégories Start with our Beginner’s Guide €"))
  #link = page.ui.link(str(bytes("Top catégories Start with our Beginner’s Guide €", 'cp1252'))
  #                    .replace(r"\xc3\xa9", "&#233;").replace(r"\xe2\x80\x99", "&#180"))
  col.add(title)
  col.add(text)
  col.add(link)
  col.style.css.border_top = "1px solid blue"
  row.append(col)

row = page.ui.row(row)
div = page.ui.div()
div.attr["class"].add("container")
div.add(row)

row.style.css.border_bottom = "1px solid blue"

page.ui.banners.text([], background="#3776ab")

text = '''
The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers.
'''

v1 = page.ui.vignets.vignet("Python Enhancement Proposals: The future of Python", text, width=(80, '%'))
#v1.style.css.background = "#2b5b84"
v1.style.css.background = "#d8dbde"

# 2020-07-23T00:00:00+00:00
dts ={
  "2020-07-23": "EuroPython 2020 Online",
  "2020-07-27": "EuroSciPy 2020 (canceled)",
      }

events = page.ui.lists.items()
for k, v in dts.items():
  dt = page.ui.tags.time(k)
  content = page.ui.text(v)
  content.style.css.margin_left = "20px"
  events.add(page.ui.div([dt, content]))


rss = page.ui.icons.rss(align="center")

v = page.ui.vignets.vignet(">>> Python Software Foundation", text, width=(80, '%'))
v.style.css.background = "#3776ab"

print("Top catégories Start with our Beginner’s Guide".encode())


