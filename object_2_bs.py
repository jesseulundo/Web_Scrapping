import urllib
from bs4 import BeautifulSoup
import ssl

#this is the SSl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = raw_input('Enter - ')
html = urllib.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
	print tag.get('href', None), tag.contents, tag.attrs
	