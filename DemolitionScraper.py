import urllib2
import cookielib
from lxml import etree
import lxml.html
import StringIO
import string
import os

# Set up cookies to work like regular browser and access entry URL to get set up properly
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
first = opener.open("http://www.indy.gov/eGov/City/DCE/Pages/Citizen%20Access%20Portal.aspx")

# Step through all cases
for case in range(1965,3777):
	url = 'http://permitsandcases.indy.gov/CitizenAccess/Cap/CapDetail.aspx?Module=HHC&TabName=HHC&capID1=11DEM&capID2=00000&capID3=%(#)05d&agencyCode=INDY&IsToShowInspection="' % {"#": case}

	f = opener.open(url)
	html = f.read()
	tree = lxml.html.fromstring(html)
	caseNumber = tree.xpath('//span[@id="ctl00_PlaceHolderMain_lblPermitNumber"]/text()')
	parcel = tree.xpath('//div[@id="ctl00_PlaceHolderMain_PermitDetailList1_palParceList"]/div[1]/div/text()')
	print "Case: %(case)s Parcel: %(parcel)s " % {"case":caseNumber, "parcel":parcel}
	i = 0
	fileName = caseNumber[0] + '-' + str(i) + '.html'
	while os.path.isfile(fileName): 
		i += 1
		fileName = caseNumber[0] + '-' + str(i) + '.html'	
	file = open(fileName, "w")	
	file.write(html)

