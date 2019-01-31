import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('track_data_base.sqlite')
cur = conn.cursor()

#creating the fresh tables using assignment scrit
cur.executescript('''
drop table if exists Artist;
drop table if exists genre;
drop table if exists Album;
drop table if exists Traks;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

#search for the XML file
fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

#function to search inside the XML file
def lookup(d, key):
	found = False
	for child in d:
		if found : return child.text
		if child.tag == 'key' and child.text == key :
			found = True
	return None
	
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
	if (lookup(entry, 'Track ID') is None ) : continue
	
	name = lookup(entry, 'Name')
	genre = lookup(entry, 'Genre')
	artist =  lookup(entry, 'Artist')
	album = lookup(entry, 'Album')
	count = lookup(entry, 'Play Count')
	rating = lookup(entry, 'Rating')
	length = lookup(entry, 'Total Time')
	
	if name is None or artist is None or album is None or genre is None :
		continue
	print( name, artist, album, count, rating, length, genre)
	#Artist table
	cur.execute('''insert or ignore into Artist (name)
		values ( ? ) ''', ( artist, ) )
	cur.execute('select id from Artist where name = ? ', (artist, ))
	artist_id = cur.fetchone()[0]
	#Genre table
	cur.execute('''insert or ignore into Genre (name)
		values ( ? )''', (genre, ))
	cur.execute('select ID from Genre where name = ? ', (genre, ))
	genre_id = cur.fetchone()[0]
	#Album table
	cur.execute(''' insert or ignore into Album (title, artist_id)
		values ( ?, ?)''', ( album, artist_id) )
	cur.execute('select id from Album where title = ? ', (album, ))
	album_id = cur.fetchone()[0]
	#Track table
	cur.execute(''' insert or replace into Track 
		(title, album_id, len, rating, count, genre_id) 
		values ( ?, ?, ?, ?, ?, ? )''', 
		( name, album_id, length, rating, count, genre_id ) )
		
	conn.commit()