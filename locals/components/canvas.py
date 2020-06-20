
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

canvas = page.ui.charts.canvas.new()
##canvas.style.css.borders_light()

#print(canvas.ctx.rotate(page.js.math.PI * 80))

page.js.onReady([
  canvas.ctx.beginPath(),
  canvas.ctx.font("20px Georgia"),
  canvas.ctx.createLinearGradient(0, 0, canvas.dom.width, 0, "test").
    addColorStop("0", "magenta").addColorStop("0.5", "blue").addColorStop("1.0", "red"),
  canvas.ctx.strokeStyle(page.js.object("test")),
  canvas.ctx.strokeText("Hello World!", 10, 50),
  # canvas.ctx.lineCap("square"),
  # canvas.ctx.font("30px Verdana"),
  # canvas.ctx.shadowBlur(10),
  # canvas.ctx.shadowColor("blue"),
  # canvas.ctx.moveTo(20, 20),
  # canvas.ctx.bezierCurveTo(20, 100, 200, 100, 200, 20),

  #canvas.ctx.strokeWeight(1),
  #canvas.ctx.strokeStyle("pink"),
  #canvas.ctx.rotate(page.js.math.PI * 80),
  #canvas.ctx.lineWidth(10),
  #canvas.ctx.moveTo(10, 30),
  #canvas.ctx.lineTo(200, 100),
  #canvas.ctx.arc(100, 75, 50, 0, page.js.math.PI * 2),
  #canvas.ctx.fill("green"),

  #canvas.ctx.fillRect(20, 20, 150, 100),
  #canvas.ctx.fillText("test", 100, 100, fillStyle="red"),
  # canvas.ctx.globalAlpha(0.1),
  # canvas.ctx.textAlign("right"),
  # canvas.ctx.fillText(["width:", canvas.ctx.measureText("Hello World").width], 10, 50),
  # canvas.ctx.textBaseline("bottom"),
  # canvas.ctx.strokeText("test", 10, 50),

  #canvas.ctx.fillStyle("orange"),
  # canvas.ctx.fillRect(10, 10, 100, 50),
  # page.js.alert(canvas.ctx.isPointInPath(10, 50)),
  #canvas.ctx.translate(70, 70),
  #canvas.ctx.fillStyle("green"),
  #canvas.ctx.scale(2, 2),
  #canvas.ctx.rotate(page.js.math.PI * 80 / 180),
  #canvas.ctx.fillRect(10, 10, 100, 50),
  canvas.ctx.stroke(),
])

