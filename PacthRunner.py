
import os
import sys
import time
import config
import traceback

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cur_dir, "..", "epyk-ui"))


from epyk.core.js import Imports
#
Imports.STATIC_PATH = "./../../static"

# To reduce the scope of filters to generate
filter = None


def process_folder(folder, results, main_folder=None):
  """

  :param folder:
  :param main_folder:

  :return:
  """
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
          config.OUT_FILENAME = "%s_%s_%s" % (main_folder, folder, script_name)
          __import__("%s.%s.%s" % (main_folder, folder, script_name))
        else:
          config.OUT_FILENAME = "%s_%s" % (folder, script_name)
          __import__("%s.%s" % (folder, script_name))
        results.append("%s.html" % os.path.join(config.OUTPUT_PATHS_LOCALS_HTML, config.OUT_FILENAME))
        count_run_scripts += 1
      except Exception as err:
        traceback.print_exception(*sys.exc_info())
        print("Error with: %s" % file)
  print("Processing %s (%s / %s reports) in %s seconds" % (folder, count_run_scripts, count_scripts, time.time() - start))


results = []
for folder in os.listdir(os.path.join(cur_dir, 'locals')):
  if os.path.isdir(os.path.join(cur_dir, 'locals', folder)) and folder != '__pycache__':
    process_folder(folder, results, main_folder='locals')

# Run other type of reports
process_folder('websites', results)
process_folder('interactives', results)
process_folder('dashboards', results)

if filter is not None:
  print("")
  print("Reports location:")
  for report in results:
    print(report)
