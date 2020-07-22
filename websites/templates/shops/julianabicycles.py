# https://www.julianabicycles.com/en-US


from epyk.core.Page import Report
from websites.material import julianabicycles_data


page = Report()
page.headers.favicon(julianabicycles_data.FAVICON)

page.ui.images.carrousel(julianabicycles_data.IMAGES, path=julianabicycles_data.IMG_PATH)
