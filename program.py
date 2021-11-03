
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
#   if key exist in dict return False
#   elif key does NOT exists return true and add to dictionary (k:v)
# def tryDelete(d, k)
#   d dictionary k key
#   if key exist in dict delete it and return it
#       if not return None
# create a dictionary of cities in the world and their population:
#   Tel-aviv, london, paris, tokyo
#    { tel-Aviv: 451,520 ,  ... }
#   input a city name from user
#     print the city number of citizens
#     if city does not exist print 'city does not exist in the dict'
#   input a number from the user
#     if there is acity with number of citizens in the dict print the city name
# def getSize(d)
#     return the size of the dictionary (number of items)
# def isDictKeysAlpha(d)
#     returns true if all the keys are alpha (hint: use isaplhpa)
# def popByValue(d, v)
#     pop all items with the v specific value
#     return a list of all of the removed items
# def printDictionary (d)
#  * etgar: use for loop on d.items()