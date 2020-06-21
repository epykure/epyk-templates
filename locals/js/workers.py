
from epyk.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()

w = page.js.worker()

w.connect(content='''
self.addEventListener('message', function(e) {
  var data = e.data;
  switch (data.cmd) {
    case 'start':
      self.postMessage('WORKER STARTED TEST: ' + data.msg);
      break;
    case 'stop':
      self.postMessage('WORKER STOPPED: ' + data.msg +
                       '. (buttons will no longer work)');
      self.close(); // Terminates the worker.
      break;
    default:
      self.postMessage('Unknown command: ' + data.msg);
  };
}, false);
''')

div = page.ui.div()

page.ui.button("Say HI").click([w.postMessage({'cmd': 'start', 'msg': 'Hi'})])
page.ui.button("Send unknown command").click([w.postMessage({'cmd': 'stop', 'msg': 'Bye'})])
page.ui.button("Stop worker").click([w.terminate()])


w.on('message', [div.build(w.message)])