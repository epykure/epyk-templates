import sys
import time

sys.path.append("../epyk-ui")


CHARTS = False
GEO = False
PACKAGES = True
COMPONENTS = True
JS = True
TABLES = False
TEXT = False
LAYOUT = True
DASH = False
WEB = False


# -------------------------------------------------------------------------------------------------------------------
# Pure Javascript
#
if JS:
  print("Processing Chart examples.... ")
  start = time.time()
  import locals.file_js_events
  import locals.file_js_transforms
  print("total time: %s" % (time.time() - start))
  print("")


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
  import locals.file_extension_google
  import locals.file_codemirror
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
  import locals.file_editor
  import locals.file_svg
  import locals.file_dates
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
  import locals.file_tables_aggrid
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
  import locals.file_paragraph
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
  import locals.file_layouts
  import locals.file_popup
  import locals.file_panels
  # import locals.file_form
  print("total time: %s" % (time.time() - start))
  print("")


# -------------------------------------------------------------------------------------------------------------------
# DASHBOARDS
#
if DASH:
  print("Processing Dashboards examples.... ")
  start = time.time()
  print("total time: %s" % (time.time() - start))
  print("")


# -------------------------------------------------------------------------------------------------------------------
# WEBSITES
#
if WEB:
  print("Processing Websites examples.... ")
  start = time.time()
  import websites.web_stackoverflow
  import websites.web_app
  import websites.web_coming_soon
  import websites.web_amazon
  import websites.web_github
  import websites.web_hotel
  import websites.web_photos
  import websites.web_restaurant
  import websites.web_social_media
  import websites.web_startup
  import websites.web_wedding
  import websites.web_wikipedia
  import websites.web_youtube
  import websites.web_google
  print("total time: %s" % (time.time() - start))
  print("")

#
# from docutils.core import publish_parts
#
# rst = publish_parts('''
#
# Usage:
# ------
# number = rptObj.ui.vignets.number(500, "Test")
# number_2 = rptObj.ui.vignets.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
# number.span.add_icon(rptObj.ui.icons.get.ICON_ENVELOPE)
#
# Related Pages:
# --------------
# https://www.w3schools.com/tags/att_input_type_number.asp
#
# Attributes:
# --------------
# :param test2: test
# :param test: test
# ''', writer_name='html')['html_body']
# print(rst)
#
# import pydoc
#
# from epyk.core.html import Html
#
# doc = pydoc.HTMLDoc()
# output = doc.docmodule(Html)
# print(output)
