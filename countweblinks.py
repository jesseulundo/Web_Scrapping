import urllib
import re
from bs4 import BeautifulSoup

url_name = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
count = int(count)
position = raw_input('Enter position: ')
position = int(position)

for x in range(0, count+1):
	html = urllib.urlopen(url_name).read()
	soup = BeautifulSoup(html, "lxml")
	while x <= count: break
	print 'Retrieving: ',url_name
	
	tags = soup('a')
	pos = 0
	for tag in tags:
		if pos == position-1:
			url_name = str(tag.get('href', None))
			break
		pos += 1