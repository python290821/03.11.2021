
# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict = {} # new dictionary
thisdict = dict() # new dictionary
thisdict['brand'] = 'Ford'
thisdict['model'] = 'Mustang'
thisdict['year'] = 1964

print(thisdict['year'])
# print(thisdict['Year']) # [ ] when key not found -- will crash
print(thisdict.get('Year'))

# keys()
print('keys: ', list(thisdict.keys()))
print('keys: ', tuple(thisdict.keys()))
# values()
print('values: ', list(thisdict.values()))
print('values: ', tuple(thisdict.values()))
print('values: ', set(thisdict.values()))

# update -- later

# remove
# thisdict['model'] = 'Mustang' -- remove
# remove and resolve
print(thisdict.pop('model'))
# print(thisdict.pop('model')) # will create an error
#del thisdict['model'] # will create an error
del thisdict['year']
print(thisdict)


# def doesKeyExist(d, k)
#   d dictionary k key
#   if key exist in dict return True else False
# def tryAdd(d, k, v)
#   if key exist in dict return True else False
#   if key exists return False
#     else add to dictionary (k,) and return True
# print dictionary (d)
#  * etgar: use for loop on d.items()