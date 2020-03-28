import sys
import time

sys.path.append("../epyk-ui")


CHARTS = True
GEO = True
PACKAGES = True
COMPONENTS = True
TABLES = True
TEXT = True
LAYOUT = True


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
  import locals.file_geo_chartjs
  import locals.file_geo_dc
  import locals.file_geo_plotly
  print("")


# -------------------------------------------------------------------------------------------------------------------
# PACKAGES
#
if PACKAGES:
  print("Processing PACKAGES examples.... ")
  import locals.file_jquery_ui
  import locals.file_d3
  import locals.file_data_vis
  import locals.file_data_crossfilter
  print("")


# -------------------------------------------------------------------------------------------------------------------
# BASIC HTML COMPONENT
#
if COMPONENTS:
  print("Processing COMPONENTS examples.... ")
  import locals.file_canvas
  import locals.file_svg
  import locals.file_list
  import locals.file_image
  import locals.file_select
  import locals.file_radio
  import locals.file_button
  import locals.file_bespoke
  print("")


# -------------------------------------------------------------------------------------------------------------------
# TABLES
#
if TABLES:
  print("Processing TABLES examples.... ")
  import locals.file_table
  import locals.file_tables_d3
  import locals.file_tables_datatable
  import locals.file_tables_tabulator
  print("")


# -------------------------------------------------------------------------------------------------------------------
# TEXT
#
if TEXT:
  import locals.file_rich_texts
  import locals.file_input
  import locals.file_texts
  import locals.file_links
  print("")


# -------------------------------------------------------------------------------------------------------------------
# LAYOUT AND NAVIGATION
#
if LAYOUT:
  import locals.file_navigation
  import locals.file_menu
  import locals.file_popup
  import locals.file_panels
  # import locals.file_form
  print("")


# -------------------------------------------------------------------------------------------------------------------
# DASHBOARDS
#


# -------------------------------------------------------------------------------------------------------------------
# WEBSITES
#
