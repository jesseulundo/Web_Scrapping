import re
import urllib 
from bs4 import BeautifulSoup

url = raw_input('Enter the URL: ')
page = urllib.urlopen(url).read()
soup = BeautifulSoup(page, "lxml")
total = 0
count = 0
tags = soup('span')
for tag in tags:
	lines = tag.decode().split()
	lines = str(tag)
	print lines
	numbers = re.findall('[0-9]+',lines)
	if len(numbers) > 0:
		for number in numbers:
			total += int(number)
			count += 1
print 'Count ',count
print 'Sum ',total 
	


