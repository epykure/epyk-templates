
import os
import sys
import uvicorn

import config

from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse


app = FastAPI(debug=True)

origins = [
    "*",
    "http://127.0.0.1",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cur_dir, "..", "..", "epyk-ui"))


@app.get('/', response_class=HTMLResponse)
def home():
  """
  Report creation on the fly in Flask
  """
  from epyk.core.Page import Report

  rptObj = Report()
  list = rptObj.ui.list()
  for pyfile in os.listdir("reports"):
    list.add_item(rptObj.ui.link(pyfile, url="/report/%s" % pyfile[:-3]).css({"padding": '2px 0', 'display': 'block'}))
  return rptObj.outs.html()


@app.get("/report/{file_name}", response_class=HTMLResponse)
def read_item(file_name):
  html_content = open(os.path.join('front_end', '%s.html' % file_name)).read()
  return html_content


@app.post("/file")
async def file(request: Request):
  import json

  data = await request.form()
  content = []
  for pyFile in data.values():
    print(pyFile.filename)
    content = json.loads(await pyFile.read())
    print(content)
    print(list(content[0].keys()))
    return {"cols": content}


@app.post("/data")
async def data(request: Request):
  from epyk.core import data as chart_data

  data = await request.json()
  result = chart_data.chartJs.xyz([
    {"x": 1, 1: 1, 2: 2},
    {"x": 2, 1: 1, 2: 2},
  ], [1, 2], 'x')
  pie_data = chart_data.chartJs.y([
    {"x": 1, 1: 1, 2: 2},
    {"x": 2, 1: 2, 2: 2},
  ], [1], 'x')

  return {"chart": result, 'pie': pie_data}


if __name__ == '__main__':
  uvicorn.run("fastapi_server:app", host=config.SERVER_DATA_HOST, port=config.SERVER_DATA_PORT, reload=True)
