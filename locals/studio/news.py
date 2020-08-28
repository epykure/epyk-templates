
from epyk_studio.core.Page import Report

# Create a basic report object
page = Report()
page.headers.dev()

page.studio.news.theme()

page.studio.news.search()


page.studio.carousel([
  "Great results",
  "Amazing Stuff"
])

page.studio.news.rates([
  [page.studio.news.comments(233, "#"), 11644.29	, -132.48, -1.12],
  ['BCH-EUR', 312.09		, 3.85	, 1.25],
])

page.studio.quiz.summary([
  ["pendu", '-', '-', '-']
])

data = [
        {"text": 'test 1', "status": 'success', 'time': '9h45'},
        {"text": 'test 2', "status": 'error', 'time': '11h45'}, # , 'size': 30
        {"text": 'test 3', "status": 'error', 'time': '12h45'},
        {"text": 'test 4', "status": 'error', 'time': '13h45'},
        {"text": 'test 5', "status": 'pending', 'time': '22h45'}]

svg = page.studio.news.stepper(data, color='yellow')

page.studio.news.miniature("How AOC Could Block Trump’s New Housing Discrimination Rules",
    "https://www.bloomberg.com/news/articles/2020-07-28/aoc-moves-to-block-trump-s-fair-housing-rule?srnd=premium-europe",
    "https://assets.bwbx.io/images/users/iqjWHBFdfxIU/itOR8PEvfY9A/v1/160x120.jpg",
    'Politics', width=(150, 'px'))

page.ui.buttons.live(10, [])

page.studio.news.audio("Listen", "#")
page.studio.news.share()
page.studio.news.comments(233, "#")
page.studio.news.section("Must see")
page.studio.news.tags(["Spain", 'Isolation'])
page.studio.news.time('2020-07-28 20:30:27.243860')
page.studio.news.border()
page.studio.news.delimiter()
page.studio.news.exchange(True, 55623.45)
page.studio.news.moves(55623.45, 55623.45)
page.studio.news.shares(True, 55623.45, [55623.45, 53623.45, 55423.45, 45623.45])
