
# https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f

# https://github.com/mozilla/geckodriver/releases

# https://booking.eurostar.com/uk-en/train-search?origin=7015400&destination=8727100&adult=1&outbound-date=2020-07-09&inbound-date=2020-07-17

from bs4 import BeautifulSoup

import time
import json
import os

from selenium import webdriver
from bs4 import BeautifulSoup

from epyk.core.Page import Report

# Create a basic report object
page = Report()
page.headers.dev()

dates = page.py.dates.range_dates("2020-08-01", "2020-12-31")
dated_path = page.py.dates.path(True)

# specify the url
# run firefox webdriver from executable path of your choice
driver = webdriver.Firefox(executable_path=r"C:\servers\browsers\geckodriver.exe")
prices = []
for date in dates:
  print(date)
  out_path = os.path.join("C:/tmps", dated_path)
  if not os.path.exists(out_path):
    os.makedirs(out_path)
  tmp_file = os.path.join(out_path, "eurostar_%s.json" % date.replace("-", ""))
  if not os.path.exists(tmp_file):
    url = 'https://booking.eurostar.com/uk-en/train-search?origin=7015400&destination=8727100&adult=1&outbound-date=%s' % date
    driver.get(url)
    time.sleep(3)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    results, row = [], {}
    categories = ['standard', 'premier', 'business']
    for i, t in enumerate(soup.find_all("section", {'class': 'train__class-of-accommodation'})):
      if i % 3 == 0 and row:
        results.append(row)
        row = {}
      if t.find("div", {"class": 'coa__price-container'}) is None:
        row[categories[i % 3]] = None
      else:
        row[categories[i % 3]] = t.find("div", {"class": 'coa__price-container'}).find("span", {"class": 'price price--gbp'}).text
    results.append(row)
    for i, t in enumerate(soup.find_all("section", {'class': 'journey-details'})):
      results[i]['time'] = t.find("li", {'class': 'item-depart'}).text
      results[i]['date'] = date
    with open(tmp_file, "w") as f:
      json.dump(results, f)
  else:
    with open(tmp_file) as f:
      results = json.load(f)
  for rec in results:
    if 'time' in rec:
      rec['full_date'] = "%s %s" % (date, rec['time'])
      for p in ['standard', 'premier', 'business']:
        rec[p] = float(rec[p][1:]) if rec[p] is not None else rec[p]
  prices.extend(results)

driver.quit()

page.ui.charts.chartJs.line(prices[::-1], y_columns=['standard', 'premier', 'business'], x_axis='full_date')
#page.ui.table(prices)

