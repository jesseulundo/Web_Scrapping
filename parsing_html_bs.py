import urllib
from bs4 import BeautifulSoup 
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
	# Look at the parts of a tag
	print 'TAG:',tag
	print 'URL:',tag.get('href', None)
	print 'Content:',tag.contents[0]
	print 'Attrs:',tag.attrs