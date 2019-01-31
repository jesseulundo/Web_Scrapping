aa = {'mike': 'male', 'kathy': 'female', 'steve': 'male', 'hillary': 'female'}
bb = {'mike': 'male', 'ben': 'male', 'hillary': 'male',}

aa.keys() & bb.keys()
aa.keys() - bb.keys()

aa.items() & bb.items()

print(aa.keys, bb.keys)