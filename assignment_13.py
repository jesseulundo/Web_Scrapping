import urllib
import xml.etree.ElementTree as ET


site_url = raw_input('Enter Location: ')
print 'Retriving ' + site_url
html = urllib.urlopen(site_url).read()
xml = ET.fromstring(html)

comments = xml.findall('.//count')

sum = 0
for count in comments:
	sum = sum + int(count.text)
	
print 'Sum: ' + str(sum)