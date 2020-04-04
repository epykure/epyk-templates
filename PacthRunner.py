import sys
import time

sys.path.append("../epyk-ui")


CHARTS = False
GEO = False
PACKAGES = False
COMPONENTS = False
TABLES = False
TEXT = True
LAYOUT = False


# -------------------------------------------------------------------------------------------------------------------
# CHARTS
#
if CHARTS:
  print("Processing Chart examples.... ")
  start = time.time()
  import locals.file_charts_dc
  import locals.file_charts_nvd3
  import locals.file_charts_vis
  import locals.file_charts_chartjs
  import locals.file_charts_sparklines
  import locals.file_charts_billboard
  import locals.file_charts_c3
  import locals.file_charts_plotly
  print("total time: %s" % (time.time() - start))
  print("")


# -------------------------------------------------------------------------------------------------------------------
# GEO
#
if GEO:
  print("Processing Geo examples.... ")
  start = time.time()
  import locals.file_geo_chartjs
  import locals.file_geo_dc
  import locals.file_geo_plotly
  print("total time: %s" % (time.time() - start))
  print("")


# -------------------------------------------------------------------------------------------------------------------
# PACKAGES
#
if PACKAGES:
  print("Processing PACKAGES examples.... ")
  start = time.time()
  import locals.file_jquery_ui
  import locals.file_jquery_ui_datepicker
  import locals.file_jquery_ui_slider
  import locals.file_jquery_ui_menu
  import locals.file_jquery_ui_autocomplete
  import locals.file_jquery_ui_progressbar
  import locals.file_timepicker
  import locals.file_d3
  import locals.file_data_vis
  import locals.file_data_crossfilter
  print("total time: %s" % (time.time() - start))
  print("")


# -------------------------------------------------------------------------------------------------------------------
# BASIC HTML COMPONENT
#
if COMPONENTS:
  print("Processing COMPONENTS examples.... ")
  start = time.time()
  import locals.file_canvas
  import locals.file_svg
  import locals.file_checkbox
  import locals.file_icons
  import locals.file_numbers
  import locals.file_list
  import locals.file_switch
  import locals.file_tree
  import locals.file_image
  import locals.file_select
  import locals.file_radio
  import locals.file_button
  import locals.file_bespoke
  print("total time: %s" % (time.time() - start))
  print("")


# -------------------------------------------------------------------------------------------------------------------
# TABLES
#
if TABLES:
  print("Processing TABLES examples.... ")
  start = time.time()
  import locals.file_table
  import locals.file_tables_d3
  import locals.file_tables_plotly
  import locals.file_tables_datatable
  import locals.file_tables_tabulator
  print("total time: %s" % (time.time() - start))
  print("")


# -------------------------------------------------------------------------------------------------------------------
# TEXT
#
if TEXT:
  print("Processing TEXT examples.... ")
  start = time.time()
  import locals.file_rich_texts
  import locals.file_input
  import locals.file_texts
  import locals.file_links
  import locals.file_vignet
  print("total time: %s" % (time.time() - start))
  print("")


# -------------------------------------------------------------------------------------------------------------------
# LAYOUT AND NAVIGATION
#
if LAYOUT:
  print("Processing LAYOUT examples.... ")
  start = time.time()
  import locals.file_navigation
  import locals.file_menu
  import locals.file_popup
  import locals.file_panels
  # import locals.file_form
  print("total time: %s" % (time.time() - start))
  print("")


# -------------------------------------------------------------------------------------------------------------------
# DASHBOARDS
#


# -------------------------------------------------------------------------------------------------------------------
# WEBSITES
#

