#from django.db import models
import requests
from lxml import html
#from clubs.models import Club


counties_page = requests.get('http://www.gaapitchlocator.net/')
counties_tree = html.fromstring(counties_page.content)
counties = counties_tree.xpath('//*[@id="map-ireland-counties"]/ul/li/a/text()')

antrim_page = requests.get('http://www.gaapitchlocator.net/provinces/ulster/antrim/#0/-60/-121')
antrim_tree = html.fromstring(antrim_page.content)
antrim_clubs = antrim_tree.xpath('//a[@title="show marker on map"]/text()')
antrim_locations = antrim_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
#armagh 
#armagh_page = requests.get('http://www.gaapitchlocator.net/provinces/ulster/armagh/#9/54.3678/-6.4600')
#armagh_tree = html.fromstring(armagh_page.content)
#armagh_clubs = armagh_tree.xpath('//a[@title="show marker on map"]/text()')
#armagh_locations = armagh_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
#Carlow
#carlow_page = requests.get('http://www.gaapitchlocator.net/provinces/leinster/carlow/#0/-60/-121')
#carlow_tree = html.fromstring(carlow_page.content)
#carlow_clubs = carlow_tree.xpath('//a[@title="show marker on map"]/text()')
#carlow_locations = carlow_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Cavan
#cavan_page = requests.get('http://www.gaapitchlocator.net/provinces/ulster/cavan/#0/-60/-121')
#cavan_tree = html.fromstring(cavan_page.content)
#cavan_clubs = cavan_tree.xpath('//a[@title="show marker on map"]/text()')
#cavan_locations = cavan_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
#Clare
#clare_page = requests.get('http://www.gaapitchlocator.net/provinces/munster/clare/#0/-60/-121')
#clare_tree = html.fromstring(clare_page.content)
#clare_clubs = clare_tree.xpath('//a[@title="show marker on map"]/text()')
#clare_locations = clare_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
###Cork
#cork_page = requests.get('http://www.gaapitchlocator.net/provinces/munster/cork/#0/-60/-121')
#cork_tree = html.fromstring(cork_page.content)
#cork_clubs = cork_tree.xpath('//a[@title="show marker on map"]/text()')
#cork_locations = cork_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Derry
#derry_page = requests.get('http://www.gaapitchlocator.net/provinces/ulster/derry/#0/-60/-121')
#derry_tree = html.fromstring(derry_page.content)
#derry_clubs = derry_tree.xpath('//a[@title="show marker on map"]/text()')
#derry_locations = derry_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Donegal
#donegal_page = requests.get('http://www.gaapitchlocator.net/provinces/ulster/donegal/#0/-60/-121')
#donegal_tree = html.fromstring(donegal_page.content)
#donegal_clubs = donegal_tree.xpath('//a[@title="show marker on map"]/text()')
#donegal_locations = donegal_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Down
#down_page = requests.get('http://www.gaapitchlocator.net/provinces/ulster/down/#0/-60/-121')
#down_tree = html.fromstring(down_page.content)
#down_clubs = down_tree.xpath('//a[@title="show marker on map"]/text()')
#down_locations = down_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Dublin
#dublin_page = requests.get('http://www.gaapitchlocator.net/provinces/leinster/dublin/#0/-60/-121') #Works
#dublin_tree = html.fromstring(dublin_page.content)
#dublin_clubs = dublin_tree.xpath('//a[@title="show marker on map"]/text()')
#dublin_locations = dublin_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
####Fermanagh
#fermanagh_page = requests.get('http://www.gaapitchlocator.net/provinces/ulster/fermanagh/#0/-60/-121')
#fermanagh_tree = html.fromstring(fermanagh_page.content)
#fermanagh_clubs = fermanagh_tree.xpath('//a[@title="show marker on map"]/text()')
#fermanagh_locations = fermanagh_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Galway
#galway_page = requests.get('http://www.gaapitchlocator.net/provinces/connacht/galway/#0/-60/-121')
#galway_tree = html.fromstring(galway_page.content)
#galway_clubs = galway_tree.xpath('//a[@title="show marker on map"]/text()')
#galway_locations = galway_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Kerry
#kerry_page = requests.get('http://www.gaapitchlocator.net/provinces/munster/kerry/#0/-60/-121')
#kerry_tree = html.fromstring(kerry_page.content)
#kerry_clubs = kerry_tree.xpath('//a[@title="show marker on map"]/text()')
#kerry_locations = kerry_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Kildare
#kildare_page = requests.get('http://www.gaapitchlocator.net/provinces/leinster/kildare/#0/-60/-121')
#kildare_tree = html.fromstring(kildare_page.content)
#kildare_clubs = kildare_tree.xpath('//a[@title="show marker on map"]/text()')
#kildare_locations = kildare_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Kilkenny
#kilkenny_page = requests.get('http://www.gaapitchlocator.net/provinces/leinster/kilkenny/#0/-60/-121')
#kilkenny_tree = html.fromstring(kilkenny_page.content)
#kilkenny_clubs = kilkenny_tree.xpath('//a[@title="show marker on map"]/text()')
#kilkenny_locations = kilkenny_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Laois
#laois_page = requests.get('http://www.gaapitchlocator.net/provinces/leinster/laois/#0/-60/-121')
#laois_tree = html.fromstring(laois_page.content)
#laois_clubs = laois_tree.xpath('//a[@title="show marker on map"]/text()')
#laois_locations = laois_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
#Leitrim
#leitrim_page = requests.get('http://www.gaapitchlocator.net/provinces/connacht/leitrim/#0/-60/-121')
#leitrim_tree = html.fromstring(leitrim_page.content)
#leitrim_clubs = leitrim_tree.xpath('//a[@title="show marker on map"]/text()')
#leitrim_locations = leitrim_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Limerick
#limerick_page = requests.get('http://www.gaapitchlocator.net/provinces/munster/limerick/#0/-60/-121')
#limerick_tree = html.fromstring(limerick_page.content)
#limerick_clubs = limerick_tree.xpath('//a[@title="show marker on map"]/text()')
#limerick_locations = limerick_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Longford
#longford_page = requests.get('http://www.gaapitchlocator.net/provinces/leinster/longford/#0/-60/-121')
#longford_tree = html.fromstring(longford_page.content)
#longford_clubs = longford_tree.xpath('//a[@title="show marker on map"]/text()')
#longford_locations = longford_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Louth
#louth_page = requests.get('http://www.gaapitchlocator.net/provinces/leinster/louth/#0/-60/-121')
#louth_tree = html.fromstring(louth_page.content)
#louth_clubs = louth_tree.xpath('//a[@title="show marker on map"]/text()')
#louth_locations = louth_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Mayo
#mayo_page = requests.get('http://www.gaapitchlocator.net/provinces/connacht/mayo/#0/-60/-121')
#mayo_tree = html.fromstring(mayo_page.content)
#mayo_clubs = mayo_tree.xpath('//a[@title="show marker on map"]/text()')
#mayo_locations = mayo_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Meath
#meath_page = requests.get('http://www.gaapitchlocator.net/provinces/leinster/meath/#0/-60/-121') #Works
#meath_tree = html.fromstring(meath_page.content)
#meath_clubs = meath_tree.xpath('//a[@title="show marker on map"]/text()')
#meath_locations = meath_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Monaghan
#monaghan_page = requests.get('http://www.gaapitchlocator.net/provinces/ulster/monaghan/#0/-60/-121')
#monaghan_tree = html.fromstring(monaghan_page.content)
#monaghan_clubs = monaghan_tree.xpath('//a[@title="show marker on map"]/text()')
#monaghan_locations = monaghan_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
#Offaly
#offaly_page = requests.get('http://www.gaapitchlocator.net/provinces/leinster/offaly/#0/-60/-121')
#offaly_tree = html.fromstring(offaly_page.content)
#offaly_clubs = offaly_tree.xpath('//a[@title="show marker on map"]/text()')
#offaly_locations = offaly_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
###Roscommon
#roscommon_page = requests.get('http://www.gaapitchlocator.net/provinces/connacht/roscommon/#0/-60/-121')
#roscommon_tree = html.fromstring(roscommon_page.content)
#roscommon_clubs = roscommon_tree.xpath('//a[@title="show marker on map"]/text()')
#roscommon_locations = roscommon_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Sligo
#sligo_page = requests.get('http://www.gaapitchlocator.net/provinces/connacht/sligo/#0/-60/-121')
#sligo_tree = html.fromstring(sligo_page.content)
#sligo_clubs = sligo_tree.xpath('//a[@title="show marker on map"]/text()')
#sligo_locations = sligo_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Tipperary
#tipperary_page = requests.get('http://www.gaapitchlocator.net/provinces/munster/tipperary/#0/-60/-121')
#tipperary_tree = html.fromstring(tipperary_page.content)
#tipperary_clubs = tipperary_tree.xpath('//a[@title="show marker on map"]/text()')
#tipperary_locations = tipperary_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Tyrone
#tyrone_page = requests.get('http://www.gaapitchlocator.net/provinces/ulster/tyrone/#0/-60/-121')
#tyrone_tree = html.fromstring(tyrone_page.content)
#tyrone_clubs = tyrone_tree.xpath('//a[@title="show marker on map"]/text()')
#tyrone_locations = tyrone_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Waterford
#waterford_page = requests.get('http://www.gaapitchlocator.net/provinces/munster/waterford/#0/-60/-121')
#waterford_tree = html.fromstring(waterford_page.content)
#waterford_clubs = waterford_tree.xpath('//a[@title="show marker on map"]/text()')
#waterford_locations = waterford_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Westmeath
#westmeath_page = requests.get('http://www.gaapitchlocator.net/provinces/leinster/westmeath/#0/-60/-121')
#westmeath_tree = html.fromstring(westmeath_page.content)
#westmeath_clubs = westmeath_tree.xpath('//a[@title="show marker on map"]/text()')
#westmeath_locations = westmeath_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Wexford
#wexford_page = requests.get('http://www.gaapitchlocator.net/provinces/leinster/wexford/#0/-60/-121')
#wexford_tree = html.fromstring(wexford_page.content)
#wexford_clubs = wexford_tree.xpath('//a[@title="show marker on map"]/text()')
#wexford_locations = wexford_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')
##Wicklow
wicklow_page = requests.get('http://www.gaapitchlocator.net/provinces/leinster/wicklow/#0/-60/-121')
wicklow_tree = html.fromstring(wicklow_page.content)
wicklow_clubs = wicklow_tree.xpath('//a[@title="show marker on map"]/text()')
wicklow_locations = wicklow_tree.xpath('//div[@class="lmm-listmarkers-panel-icons"]//a[@title="Get directions"]//@href')

# counties[9] = Dublin

for index in range(len(antrim_clubs)):
	print("db.execSQL(INITIAL_"+counties[index].upper()+"_CLUB_INSERTS);")
	print("\"('32','"+ antrim_clubs[index] +"','N/A','N/A','" + antrim_clubs[index] + "','N/A'),\" +")
	p = Club(name=Dublin_clubs[index], location=Dublin_locations[index], county='Dublin', province='Leinster')
	p.save()

#"('10',Dublin_clubs[index],'N/A','N/A',Dublin_locations[index],'N/A')," +
#"('22','Moylagh','N/A','N/A','53.7339336,-7.1522973','N/A')," +
