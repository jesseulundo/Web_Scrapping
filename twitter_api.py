from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute(''' 
			CREATE TABLE IF NOT EXISTS Twitter
			(name TEXT, retrieved INTEGER, friends INTEGER)''')
#ignoring the ssl protocol			
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#this command will verify the existence of the twitter account
while True:
	acct = input('Enter a twitter account, or quit: ')
	if (acct == 'quit'): break
	if (len(acct) < 1):
		cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
		try:
			acct = cur.fetchone()[0]
		except:
			print('No unretrieved Twitter accounts found')
			continue
	#matching the url of the account name		
	url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
	print('Retrieving', url)
	#making the connection using the url retrieved
	connection = urlopen(url, context=ctx)
	data = connection.read().decode()
	#in case headers of url are needed we create a dictionary to be retrieve the web data 
	hearders = dict(connection.getheaders())
	
	print('Remaining' , headers['x-rate-limit-remaining'])
	js = json.loads(data)
	cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))
	
	countnew = 0
	countold = 0
	
	
	for u in js['users']:
		friend = u['screen_name']
		print(friend)
		cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',(friend, ))
		try:
			count = cur.fetchone()[0]
			cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',(count+1, friend))
			countold = countold + 1
		except:
			cur.execute('''INSERT INTO Twitter (name, retrieved, friends) VALUES (?, 0, 1)''', (friend, ))
			countnew = countnew + 1
		print('New accounts=', countnew, ' revisited=', countold)
		conn.commit()
			
			
cur.close()