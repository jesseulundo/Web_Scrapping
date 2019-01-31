import xml.etree.ElementTree as ET
data = '''
	<person>
		<name>Jesse</name>
		<task>
			9:00~12:00 : Continue working on the Anaconda interface
			13:00~14:30 : Comparison study Python 2.7 and Python 3
			14:30~17:30 : Re-do Python lessons 
		</task>
		<quote hide="yes"/>
	</person>'''
tree = ET.fromstring(data)
print 'Name:',tree.find('name').text
print "Today's Task:",tree.find('task').text
print "[Today's Single word]"
print 'Fun coding? ',tree.find('quote').get('hide')

