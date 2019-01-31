import re
import urllib 
from bs4 import BeautifulSoup

url = raw_input('Enter the URL: ')
page = urllib.urlopen(url).read()
soup = BeautifulSoup(page, "lxml")
all  = soup.findAll('span',{'class':'comments'},text=re.compile(r'[0-9]{0,4}'))
cleaned = filter(lambda x: x!=u'\n',all)[4:]
print cleaned