
import os
import sys

from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse


app = FastAPI(debug=True)

origins = [
    "*",
    "http://localhost",
    "http://localhost:8080",
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


@app.post("/data")
async def data(request: Request):
  data = await request.json()
  return data
