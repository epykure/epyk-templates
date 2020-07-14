# https://www.w3schools.com/w3css/tryw3css_templates_hotel.htm
# https://www.marriott.co.uk/default.mi?program=spg

from epyk.core.Page import Report#


page = Report()

test = page.ui.div('''
As the saying goes, the best things in life are free. And our free Wedding Website is one of them. Why? Easy-to-get wedding info. RSVPs in a click. New, beautifully-designed Wedding Website templates that are practically made for you. Slide your registry in there too to take the guesswork out of gifting. Your free Wedding Website is the best way to rally your guests hands down.
''').css({"padding": '5px'})

pts = page.ui.lists.points(["WW", "test"], align="center")

sliding = page.ui.panels.slidings.right([pts, test], title="test", align="center", options={"icon_position": "right"})

#sliding.options.icon_closed = "fas fa-chevron-up"
#sliding.options.icon_expanded = "fas fa-chevron-down"
#sliding.style.css.width = "80%"
#sliding.style.css.border_bottom = "1px solid black"
#hr = page.ui.layouts.hr(width=(80, '%'))
#hr.style.css.margin = "auto"
#hr.style.css.display = "block"
