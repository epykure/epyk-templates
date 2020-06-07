
import os
import sys
import random

from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cur_dir, "..", "..", "epyk-ui"))

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


# Basic Flask Entry points
@app.route('/', methods=['GET'])
def home():
  """
  Report creation on the fly in Flask
  """
  from epyk.core.Page import Report

  rptObj = Report()
  list = rptObj.ui.list()
  for pyfile in os.listdir("reports"):
    if pyfile.startswith("socket_"):
      list.add_item(rptObj.ui.link(pyfile, url="/report/%s" % pyfile[:-3]).css({"padding": '2px 0', 'display': 'block'}))
  return rptObj.outs.html()


@app.route('/report/<file_name>')
def report(file_name):
    html_content = open(os.path.join('front_end', '%s.html' % file_name)).read()
    return render_template_string(html_content, title='Projects')


# Dedicated Socket Entry points
@socketio.on('my event', namespace='/test')
def test_message(message):
  emit('my response', {'data': message})


@socketio.on('message', namespace='/test')
def test_message(message):
  print("New Message received - %s " % message)


@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
  emit('my response', {'data': message}, broadcast=True)


@socketio.on('connect', namespace='/test')
def test_connect():
  emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
  print('Client disconnected')


# Dedicated Socket Entry points
@socketio.on('new news', namespace='/news')
def new_news(message):
  values = getSeries(5, 100)
  result_pie = chart_data.chartJs.y(values, [1, 4, 5], 'g')
  emit('news received', {"content": message, 'pie': result_pie}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, port=5010, debug=True)
