import socket 
try:
	url = raw_input('Enter the URL: ')
	port = url.split("/")
	port = port[2]
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect((port, 80))
	mysock.send('GET '+url+'HTTP/1.0\n\n')
	count = 0
	doc = ''
	while True:
		data = mysock.recv(512)
		if (len(data) < 1 ):
			break
		doc = doc + data
		count += len(data)
		
		
	mysock.close()
	pos = doc.find("\r\n\r\n")
	doc = doc[pos+4:]
	doc = doc[:3000]
	print doc
	print "Number of characters:",count
except:
	print 'Erro, enter a valid URL'
	