stuff = list()
stuff.append('python')
stuff.append('Jesse')
stuff.sort()
print (stuff[0])

print (stuff.__getitem__(0))
print (list.__getitem__(stuff,0))
print (dir(stuff))
