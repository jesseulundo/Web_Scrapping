import urllib,json


comment_sum = 0
try:
	while True:
		site_url = raw_input('Enter location: ')
		if len(site_url) < 1: break

		print 'Retrieving ',site_url
		url_handle = urllib.urlopen(site_url)
		data = url_handle.read()

		print 'Retrieved',len(data),'characters'
		json_data = json.loads(data)
		
		comment_count = len(json_data['comments'])
		print 'Count:',comment_count
		
		for comment in json_data['comments']:
			comment_sum = comment_sum + int(comment['count'])
		print 'Sum:',comment_sum
except:
	print 'JSON file does not exist!'
	exit()
	