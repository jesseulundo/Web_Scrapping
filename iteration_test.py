def printMultiples(n, high):
	i = 1
	while i <= high:
		print n*1,'\t',
		i = i + 1
	print 
	def printMultTable(high):
		i = 1
		while i <= 6:
			printMultiples (i,high)
			i= i+1
printMultiples(7, 7)