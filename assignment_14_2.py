import sqlite3

#creating the database 
conn = sqlite3.connect('emaildb.sqlite')
#opening the file 
cur = conn.cursor()
#incase table already exists
cur.execute('''
DROP TABLE IF EXISTS Counts''')
#creating the table
cur.execute('''CREATE TABLE Counts(org TEXT, count INTERGER)''')
#searching for possible file entered by the user
fname = raw_input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: '): continue
	pieces = line.split()#split the lines in group of words
	email = pieces[1]#look at the word in position 1 of the string
	org = email.split('@')[1]#split the words into different segments
	cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
	row = cur.fetchone()
	if row is None:
		cur.execute('''INSERT INTO Counts (org, count)
				VALUES (?, 1)''', (org,))
	else:
		cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
					(org,))
conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
	print(str(row[0]), row[1])

cur.close()
