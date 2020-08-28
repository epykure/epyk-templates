
from epyk_studio.core.Page import Report

# Create a basic report object
page = Report()
page.headers.dev()

page.studio.blog.theme()


#page.body.template.style.css.border = "1px solid black"

main_banner = page.ui.images.background("https://www.fitbit.com/content/dam/fitbit/global/marketing-pages/home/tablet/4thofjuly-hero-tablet.jpg/jcr:content/renditions/4thofjuly-hero-tablet-1x.jpg", height=300)

nav = page.ui.navbar(logo="https://www.fitbit.com/content/dam/fitbit/logo/FITBIT%20LOGO%20FOR%20HEADER.svg", options={"logo_width": 140})
nav.no_background()
page.body.header.add(nav)
page.body.header.add(main_banner)

title = page.studio.blog.title('''
Using data from the conversation on Twitter to help detect wildfires
''')
page.body.header.add(title)
page.studio.blog.by("Epykure", "2020-08-05")

page.ui.delimiters.dashed(width=50)

page.studio.blog.quote('''
Qualys is helping us identify our assets with Global IT Asset Inventory and the upgrades to patch management that will help us identify more deeply the missing patches and devices that we may not have seen previously due to not knowing they were there.
''', "Martin", "Developer")


page.studio.blog.italic('''
Mayday.ai combines data from the conversation on Twitter with satellite imagery, cameras, and IP911 to help provide real-time or near real-time wildfire disaster and incident management services.
''')

page.studio.blog.time("2018-08-01 16:45:21.45")



page.studio.blog.paragraph('''
# This is Title

## This is Title

In 2019, in California alone, [6,872 fire incidents](https://disasterphilanthropy.org/disaster/2019-california-wildfires/) burned more than 253,321 acres, damaged or destroyed 732 structures, and killed three people. 
When it [comes](to wildfires), early detection can buy authorities time to warn impacted communities and get the right resources in the right place quickly. Up until now, first responders and disaster response coordinators have lacked easy access to real-time, on-the-ground data. Kian Mirshahi, founder of Mayday.ai, is passionate about democratizing access to disaster information and is working to build a community-level ecosystem for proactive disaster management and resiliency. 
''', css={'External link': {"color": 'red'}})


page.studio.blog.paragraph('''
- [Faire une croisière sur la Tamise](https://www.getyourguide.com/london-l57/westminster-to-greenwich-sightseeing-cruise-t71379/?partner_id=8KYYIU8&utm_medium=online_publisher&utm_source=lespetitesjoiesdelondres%40gmail.com&placement=content-middle&cmp=Londres-En-Apr), de Westminster à Greenwich                          
''')

p1 = page.studio.blog.picture("http://www.lespetitesjoiesdelavielondonienne.com/wp-content/uploads/2020/06/Londres-en-Aout-Regent-st-1140x1520.jpg",
                            label='''
Now bringing the unified power of the Qualys Cloud Platform to Endpoint Detection & Response!
''')

page.studio.blog.center("Bonnes adresses à Londres en Août")

p2 = page.studio.blog.video(r"C:\Users\olivier\Pictures\iphone\SGHV5530.MP4", '''
Now bringing the unified power of the Qualys Cloud Platform to Endpoint Detection & Response!
''')

row = page.ui.row([p1, p2], position="top")
page.studio.banner(row)

page.studio.blog.center("Logement")

page.studio.blog.youtube("https://www.youtube.com/embed/dfiHMtih5Ac")


page.studio.blog.paragraph('''
Hotel:  Booking.com offre toutes les options pour tous les budgets. Pour les budgets plus serrés,  Travelodge est souvent une bonne option. C’est une chaîne d’hôtels à prix abordables au UK située aux quatre coin de Londres, dont le centre. En décembre, les chambres risques d’être vite prises d’assaut.

Airbnb: Si vous n’avez jamais utilisé Airbnb, vous pouvez aussi utiliser mon lien de parrainage et économiser £25 (Environ 27€) sur votre réservation. Cliquez ici.                              
''')