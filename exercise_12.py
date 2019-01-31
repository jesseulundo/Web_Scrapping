import socket 
try:
	url = raw_input('Enter the URL: ')
	port = url.split("/")
	port = port[2]
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect((port, 80))
	mysock.send('GET '+url+'HTTP/1.0\n\n')
	
	while True:
		data = mysock.recv(512)
		if (len(data) < 1 ):
			break
		print data;
		
	mysock.close()
except:
	print 'Erro, enter a valid URL'
	