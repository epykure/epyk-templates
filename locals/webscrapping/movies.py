

from bs4 import BeautifulSoup

from epyk.core.Page import Report

# Create a basic report object
page = Report()
page.headers.dev()


url_page = "http://www.allocine.fr/recherche/?q=matrix"

data = page.py.requests.webscrapping(url_page)
soup = BeautifulSoup(data, features="lxml")

for h2 in soup.find_all("h2", {"class": 'meta-title'}):
  print(h2.span.text)

for rec in soup.find_all("div", {"class": 'content-txt'}):
  print(rec.text)


