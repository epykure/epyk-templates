
from bs4 import BeautifulSoup

from epyk.core.Page import Report

# Create a basic report object
page = Report()
page.headers.dev()

# data = page.py.requests.webscrapping("https://www.amazon.fr/Marque-Amazon-Mdr40725-d%C3%A9contract%C3%A9es-Multicolore/dp/B07WKBPP5M?pf_rd_r=2KB22NERFVTGJ3C5CPAV&pf_rd_p=406ea926-3271-47c8-a9da-357e731be6bc&pd_rd_r=57ea9ff1-c6d2-4d8a-ac27-d28397a920b1&pd_rd_w=NaVHM&pd_rd_wg=iN40R&ref_=pd_gw_unk")
# soup = BeautifulSoup(data, features="lxml")
#
# # priceblock_ourprice
# print(soup.find(id="priceblock_ourprice"))

#data = page.py.requests.webscrapping("https://www.amazon.fr/s?k=disque+dur+externe&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=Q6CPWFW3ZVV0&sprefix=disqu%2Caps%2C170&ref=nb_sb_ss_i_1_5")
data = page.py.requests.webscrapping("https://www.amazon.co.uk/s?k=CPU")
soup = BeautifulSoup(data, features="lxml")

#products = [t.text for t in soup.find_all("span", {"class": "a-size-medium a-color-base a-text-normal"})]
#products2 = [t.text for t in soup.find_all("span", {"class": "a-size-base-plus a-color-base a-text-normal"})]
#print(len(products))
#print(len(products2))

#prices = [float(t.text.replace(",", ".")) for t in soup.find_all("span", {"class": "a-price-whole"})]
#print(len(prices))

amazon_prices, prds = [], set()
for t in soup.find_all("div", {'class': 'sg-row'}):
  product = t.find("span", {"class": "a-size-medium a-color-base a-text-normal"})
  price = t.find("span", {"class": "a-price-whole"})
  if product is not None and price is not None and product.text not in prds:
    amazon_prices.append({"name": product.text, 'value': price.text})
    prds.add(product.text)

for t in soup.find_all("div", {'class': 'a-row'}):
  product = t.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"})
  price = t.find("span", {"class": "a-price-whole"})
  if product is not None and price is not None and product.text not in prds:
    amazon_prices.append({"name": product.text, 'value': price.text})
    prds.add(product.text)

page.ui.table(amazon_prices)
