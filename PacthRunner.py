
import os
import sys
import time
import config
import traceback

cur_dir = os.path.dirname(os.path.abspath(__file__))


from epyk.core.js import Imports
from epyk.core.py import PyRest

PyRest.TMP_PATH = config.OUTPUT_TEMPS

Imports.STATIC_PATH = "./../../static"

# To reduce the scope of filters to generate
filter = None #
category = None # 'angular, vue'

SUCCESS = 0
FAILURE = 0


def process_folder(folder, results, main_folder=None, out_path=config.OUTPUT_PATHS_LOCALS_HTML):
  """

  :param folder:
  :param main_folder:

  :return:
  """
  global SUCCESS, FAILURE

  start, count_scripts, count_run_scripts = time.time(), 0, 0
  if main_folder is not None:
    script_path = os.path.join(cur_dir, main_folder, folder)
  else:
    script_path = os.path.join(cur_dir, folder)
  for file in os.listdir(script_path):
    if file.endswith(".py") and file != "__init__.py":
      count_scripts += 1
      if filter is not None and not filter in file:
        continue

      script_name = file[:-3]
      try:
        if main_folder is not None:
          if main_folder == 'interactives':
            config.OUT_FILENAME = script_name
          else:
            config.OUT_FILENAME = "%s_%s_%s" % (main_folder, folder, script_name)
          mod = __import__("%s.%s.%s" % (main_folder, folder, script_name), fromlist=['object'])
        else:
          config.OUT_FILENAME = "%s_%s" % (folder, script_name)
          mod = __import__("%s.%s" % (folder, script_name), fromlist=['object'])
        output = mod.page.outs.html_file(path=out_path, name=config.OUT_FILENAME)
        results.append(output)
        #results.append("%s.html" % os.path.join(config.OUTPUT_PATHS_LOCALS_HTML, config.OUT_FILENAME))
        count_run_scripts += 1
        SUCCESS += 1
      except Exception as err:
        traceback.print_exception(*sys.exc_info())
        print("Error with: %s" % file)
        FAILURE =+ 1
  if filter is None:
    print("Processing %s (%s / %s reports) in %s seconds" % (folder, count_run_scripts, count_scripts, time.time() - start))

results = []
if category is None or category == 'locals':
  for folder in os.listdir(os.path.join(cur_dir, 'locals')):
    if os.path.isdir(os.path.join(cur_dir, 'locals', folder)) and folder != '__pycache__':
      process_folder(folder, results, main_folder='locals')

# Run other type of reports
for cat in ['websites', 'dashboards']:
  if category is None or category == cat:
    if filter is None:
      print("")
      print("processing - %s" % cat)
    process_folder(cat, results)

for cat in ['interactives']:
  if category is None or category == cat:
    if filter is None:
      print("")
      print("processing - %s" % cat)
    process_folder("reports", results, main_folder=cat, out_path=config.OUTPUT_PATHS_LOCALS_INTERACTIVE)

if category in ['angular', 'vue']:

  web_frameworks = {
    'angular': {
      'out_path': config.ANGULAR_APP_PATH,
      'folder': 'src/app/apps',
      'auto_route': True},
    'vue': {
      'out_path': config.VUE_APP_PATH,
      'folder': 'src/views',
      'auto_route': True},
    'local': {
      'out_path': config.OUTPUT_PATHS_LOCALS_TS,
      'folder': category,
      'auto_route': False},
  }

  for cat in ['angular']:
    script_path = os.path.join("web", cat)
    mod = __import__("web.%s.exports" % cat, fromlist=['object'])

    #
    if web_frameworks[category]['out_path'] is not None:
      paths = web_frameworks[category]
    else:
      paths = web_frameworks['local']

    for script in mod.REPORTS:
      script_name = script[-1][:-3]
      py_script = __import__("%s.%s" % (".".join(script[:-1]), script_name), fromlist=['object'])
      py_script.page.outs.publish(server=category, app_path=paths['out_path'], selector=script_name,
                                  target_folder=paths['folder'], auto_route=paths['auto_route'])

# if category is None or category == 'locals':
# process_folder('websites', results)
# process_folder('interactives', results)
# process_folder('dashboards', results)
# process_folder('web', results)


if filter is not None:
  if filter is None:
    print("")
    print("Reports location:")
  for report in results:
    print(report)

print("")
print("Success: %s" % SUCCESS)
print("failure: %s" % FAILURE)