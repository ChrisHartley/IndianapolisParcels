import urllib2
import cookielib
from lxml import etree
import lxml.html
import StringIO
import string
import glob
import csv

csvFile = "properties-12.csv"
fileWriter = csv.writer(open(csvFile, 'wb'), dialect='excel')

htmlFiles = glob.glob('fetchThemAll/DEM12-*.html')
htmlFiles.sort()	
fileWriter.writerow(['FileName', 'Case Number', 'Parcel Number', 'PropertyAddress', 'Structure', 'Report'])
for htmlFile in htmlFiles:
	fileName = open(htmlFile, 'r')
	html = fileName.read()
	tree = lxml.html.fromstring(html)
	print htmlFile
	if not tree.xpath('//*[@id="ctl00_PlaceHolderMain_systemErrorMessage_lblMessageTitle"]/text()'):
	#if not error[0] == 'An error has occurred.':
		print "No error, proceeding"
		caseNumber = tree.xpath('//span[@id="ctl00_PlaceHolderMain_lblPermitNumber"]/text()')
		parcel = tree.xpath('//div[@id="ctl00_PlaceHolderMain_PermitDetailList1_palParceList"]/div[1]/div/text()')
		address = tree.xpath('//table[@id="tbl_worklocation"]/tr[1]/td/text()')
		propertyAddress = address[0]+address[1] if len(address) > 2 else address[0]
		propertyAddress = ' '.join(propertyAddress.split())
		structure = ' '.join(tree.xpath('//div[@id="ctl00_PlaceHolderMain_PermitDetailList1_phPlumbingGroup"]/div[2]/table[1]/tr[3]/td/span[1]/text()'))
		report = ' '.join(tree.xpath('//table[@class="ACA_TableWordBreak"][1]//span/text()'))
		try: 
			fileWriter.writerow([htmlFile, caseNumber[0], parcel[0], propertyAddress, structure, report])	
		except IndexError:
			fileWriter.writerow([htmlFile, caseNumber[0], parcel[0], propertyAddress, structure, report])
		print htmlFile
		print caseNumber
		print parcel
		print propertyAddress
		print structure
		print report
	fileName.close()

