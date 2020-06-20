
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

# Console component
c = page.ui.rich.console("This is a log section for all the events in the different buttons *")

page.ui.text("this is a test").popover("test")
page.ui.texts.label("this is a test", color="red").css({"float": 'none'})
page.ui.texts.span("Test").css({"border": "1px solid black"})
page.ui.texts.highlights("Test content", title="Test", icon="fab fa-angellist")
page.ui.texts.formula("$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$", helper="This is a formula")
page.ui.texts.paragraph("This is a paragraph", helper="Paragraph helper")
page.ui.texts.up_down({'previous': 240885, 'value': 240985})
page.ui.texts.number(289839898, label="test", helper="Ok", icon="fas fa-align-center")
page.ui.title("Test")
page.ui.title("Test", level=2)
page.ui.texts.fieldset("legend")
page.ui.layouts.hr(3)
page.ui.images.badge("This is a badge", background_color="red", color="white")
page.ui.layouts.new_line()
page.ui.images.icon("fab fa-angellist")

page.ui.fields.textarea()

quotation = page.ui.texts.blockquote("If you decide to design your own language, there are thousands of sort **of amateur language** designer pitfalls.", author="Guido van Rossum", options={"markdown": True})
quotation.style.css.padding = "0 50px"

# python = page.ui.codes.python('''
# def test(a):
#   print("Ok")
#
# ''')

f = page.ui.texts.fieldset("fieldset")
f += page.ui.title("test")
f += page.ui.texts.label("label")

pre = page.ui.texts.preformat("This is a **pre formatted text** ok", options={"markdown": True})


page.ui.texts.highlights("Test content", title="Test")

n = page.ui.numbers.pound(4647666876)
n = page.ui.numbers.euro(4647666876)


page.ui.button("Test").click([
  f.build("Ok", {"css": {"color": 'red'}}),
  f[0].build("new title"),
  c.dom.write(pre.dom.content),
  n.build(34.5656),
#   python.build('''
# def function(test):
#   print("RRRRRRRRRRRR")
# ''')
])

c.move()

#page.ui.texts.blockquote("This is a code")
#page.ui.texts.preformat("This is a pre formatted text")
#page.ui.texts.code("This is a code")

