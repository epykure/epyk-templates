import json
import os
import random

from flask import render_template_string
from flask import Flask
app = Flask(__name__)


from epyk.core import data as chart_data


def getSeries(count, size, negatives=0.1, missing=0.2):
  data = []
  #
  neg = size * [False]
  miss = size * [False]
  for s in range(size):
    data.append({"x": s, 'r': random.randint(0, 10), 'g': random.randint(0, 5)})
    for c in range(count):
      if miss[s]:
        continue

      data[-1][c] = random.randint(0, 10000) / 100 * (-1 if neg[s] else 1)
  return data


@app.route('/data_plotly_3d', methods=['POST'])
def data_plotly_3d():
    data1, data2 = [], []
    for j in range(15):
      data1.append([random.randint(6, 10) for i in range(6)] )
    for j in range(15):
      data2.append( [random.randint(0, 5) for i in range(6)] )
    return json.dumps(chart_data.plotly.map([data1, data2]))


@app.route('/data_plotly', methods=['POST'])
def data_plotly():
    values = getSeries(5, 100)
    result = chart_data.plotly.xy(values, [1, 2], 'x')
    result_bar = chart_data.plotly.xy(values, [3, 4, 5], 'g')
    result_pie = chart_data.plotly.xy(values, [1], 'g')
    return json.dumps({'scatter': result, 'pie': result_pie, 'bar': result_bar})


@app.route('/data_nv', methods=['POST'])
def data_nvd3():
    values = getSeries(5, 100)
    result = chart_data.nvd3.xy(values, [1, 2, 3], 'x')
    result_bar = chart_data.nvd3.labely(values, [3, 4, 5], 'g')
    result_pie = chart_data.nvd3.xy(values, [1], 'g')
    return json.dumps({'scatter': result, 'pie': result_pie, 'bar': result_bar})


@app.route('/data_chartjs', methods=['POST'])
def data_chartJs():
    values = getSeries(5, 100)
    result = chart_data.chartJs.xyz(values, [1, 2], 'x')
    result_bar = chart_data.chartJs.y(values, [3, 4, 5], 'g')
    result_pie = chart_data.chartJs.y(values, [1, 4, 5], 'g')
    return json.dumps({'scatter': result, 'pie': result_pie, 'bar': result_bar})


@app.route('/data_c3', methods=['POST'])
def data_c3():
    values = getSeries(5, 30)
    result = chart_data.c3.y(values, [1, 2], 'x')
    result_bar = chart_data.c3.y(values, [3, 4, 1], 'g')
    result_pie = chart_data.c3.y(values, [1, 4, 5], 'g')
    return json.dumps({'scatter': result, 'pie': result_pie, 'bar': result_bar})


@app.route('/report/<file_name>')
def report(file_name):
    html_content = open(os.path.join('front_end', '%s.html' % file_name)).read()
    return render_template_string(html_content, title='Projects')

