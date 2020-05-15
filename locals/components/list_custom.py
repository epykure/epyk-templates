from epyk.core.Page import Report

import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Stepper data
records = []
for i in range(6):
  records.append({'text': 'test %s' % i, 'color': 'red', 'icon': 'fas fa-bolt'})

# Create a stepper
lt = rptObj.ui.lists.items(records)
lt.add_type("bespoke", '''
var item = document.createElement("DIV"); 

var span = document.createElement("SPAN");  
span.setAttribute('name', 'value'); span.setAttribute('data-valid', true);
span.style.color = data.color;

var icon = document.createElement("I"); 
if(typeof data.icon !== 'undefined') {data.icon.split(" ").forEach(function(s){icon.classList.add(s)})}
icon.style.margin = '2px 5px';

item.appendChild(icon); 
item.appendChild(span); 

if(options.click != null){ 
  item.style.cursor = 'pointer';
  item.onclick = function(event){ var value = this.innerHTML; options.click(event, value) }};
if(typeof data === 'object'){ span.innerHTML = data.text} else { span.innerHTML = data }
''', dependencies=['font-awesome'])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)