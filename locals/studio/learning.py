
from epyk_studio.core.Page import Report#

page = Report()
page.headers.dev()

page.ui.title("Print messages")

# Python version
import sys
page.ui.print('Python: {}'.format(sys.version))
# scipy
import scipy
page.ui.print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
page.ui.print('numpy: {}'.format(numpy.__version__))
# matplotlib
# pandas
import pandas
page.ui.print('pandas: {}'.format(pandas.__version__))

t = page.ui.title("Fibonacci Algorithm")

page.ui.button("click").click([
  t.build("rree", profile={"name": 'test'})
])

def fib(n):
  """

  :param n:
  :return:
  """
  a, b = 0, 1
  while a < n:
    page.ui.print(a, end=' ')
    a, b = b, a+b


page.ui.print(fib)

page.body.onReady([
  page.js.console.log(page.js.location.urlSearchParams.get("a"))
])
fib(20)

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)


page.ui.title("Dataset")

t1 = page.studio.dashboard.table(dataset.to_dict('records'))
page.ui.print(dataset.shape)
t2 = page.studio.dashboard.table(dataset.head(20).to_dict('records'))
t3 = page.studio.dashboard.table(dataset.describe().to_dict('records'))

page.ui.title("Dataset details")
page.studio.row([t2, t3], position="top")

l = page.studio.dashboard.line(dataset.to_dict('records'),
  y_columns=["sepal-width"],
  x_axis='sepal-length'
)

b = page.studio.dashboard.box(dataset.to_dict('records'),
  y_columns=["sepal-width", "petal-width"], x_columns=['sepal-length']
)

s = page.studio.dashboard.radar(dataset.to_dict('records'),
  y_columns=["sepal-width"],
  x_axis='sepal-length'
)

page.studio.row([l, b, s], position="top")