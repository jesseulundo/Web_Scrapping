import sqlite3

conn = sqlite3.connect('music.sqlite')#creating the DB command
cur = conn.cursor()#opening file command

cur.execute('drop table if exists Tracks')#in case a similar table exists this command will drop the existing table
cur.execute('create table Tracks (Title text, Plays integer)')#this command will create a new table into the database
#this commands will insert data into the table 
cur.execute('insert into Tracks (Title, Plays) values (?, ?)', ('My Way', 15))
cur.execute('insert into Tracks (Title, Plays) values (?, ?)', ('Thundertruck', 20))
cur.execute('insert into Tracks (Title, Plays) values (?, ?)', ('A mulher tem forca', 18))
cur.execute('insert into Tracks (Title, Plays) values (?, ?)', ('lixo', 102))
#this command will add the elements to the table
conn.commit()

print('Tracks:')
cur.execute('select Title, Plays from Tracks')#this command will make it possible to view the items in the table 
#execute the for loop to be able to run through the tables contents and print them out 
for row in cur:
	print(row)
	
cur.execute('delete from Tracks where Plays > 100')
conn.commit()
conn.close()