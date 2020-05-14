
from epyk.core.Page import Report

import config

# Create a basic report object
rptObj = Report()

d3s = rptObj.ui.charts.d3.script(
  'cloud',
  [
    "https://cdnjs.cloudflare.com/ajax/libs/d3-cloud/1.2.5/d3.layout.cloud.min.js",
   ],
)

d3s.loader('''
var layout = d3.layout.cloud().size([options.wdith, options.height])
    .words(data.map(function(d) { return {text: d, size: 10 + Math.random() * 90}; }))
    .padding(5).rotate(function() { return ~~(Math.random() * 2) * 90; })
    .font("Impact").fontSize(function(d) { return d.size; }).on("end", draw);
layout.start();

function draw(words) {
  htmlObj.append("svg")
      .attr("width", layout.size()[0]).attr("height", layout.size()[1])
    .append("g")
      .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
    .selectAll("text")
      .data(words)
    .enter().append("text")
      .style("font-size", function(d) { return d.size + "px"; })
      .style("font-family", "Impact")
      .attr("text-anchor", "middle")
      .attr("transform", function(d) {
        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
      })
      .text(function(d) { return d.text; });
};

''')

d3s.data("This sn example of text in the world cloud")

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
