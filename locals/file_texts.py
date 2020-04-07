
from epyk.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

rptObj.ui.text("this is a test")
rptObj.ui.texts.label("this is a test", color="red").css({"float": 'none'})
rptObj.ui.texts.span("Test").css({"border": "1px solid black"})
rptObj.ui.texts.highlights("Test content", title="Test", icon="fab fa-angellist")
rptObj.ui.texts.formula("$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$", helper="This is a formula")
rptObj.ui.texts.paragraph("This is a paragraph", helper="Paragraph helper")
rptObj.ui.texts.up_down({'previous': 240885, 'value': 240985})
rptObj.ui.texts.number(289839898, label="test", helper="Ok", icon="fas fa-align-center")
rptObj.ui.title("Test")
rptObj.ui.title("Test", level=2)
rptObj.ui.texts.fieldset("legend")
rptObj.ui.layouts.hr(3)
rptObj.ui.images.badge("This is a badge", background_color="red", color="white")
rptObj.ui.layouts.new_line()
rptObj.ui.images.icon("fab fa-angellist")

quotation = rptObj.ui.texts.blockquote("If you decide to design your own language, there are thousands of sort of amateur language designer pitfalls.", author="Guido van Rossum")
quotation.style.css.padding = "0 50px"

python = rptObj.ui.codes.python('''
def test(a):
  print("Ok")

''')

f = rptObj.ui.texts.fieldset("fieldset")
f += rptObj.ui.title("test")
f += rptObj.ui.texts.label("label")

pre = rptObj.ui.texts.preformat("This is a pre formatted text")


rptObj.ui.texts.highlights("Test content", title="Test")

n = rptObj.ui.numbers.pound(4647666876)
n = rptObj.ui.numbers.euro(4647666876)


rptObj.ui.button("Test").click([
  f.build("Ok", {"css": {"color": 'red'}}),
  f[0].build("new title"),
  c.write(pre.dom.content),
  n.build(34.5656),
  python.build('''
def function(test):
  print("RRRRRRRRRRRR")
''')
])

c.move()

#rptObj.ui.texts.blockquote("This is a code")
#rptObj.ui.texts.preformat("This is a pre formatted text")
#rptObj.ui.texts.code("This is a code")

print(rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name="report_text"))
