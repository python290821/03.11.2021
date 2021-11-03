
# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "age": 1964
}
for k in thisdict:
  print(f'[{k}]: [{thisdict[k]}]')

for k in thisdict.keys():
  print(f'key={k}: value={thisdict[k]}')

for k in thisdict.keys():
  v = thisdict[k]
  print(f'key={k}: value={v}')

for k,v in thisdict.items():
  print(f'key={k}: value={v}')

for v in thisdict.values():
  if v == 1964:
    # stuck
    pass

for k in thisdict.keys():
  v = thisdict[k]
  if v == 1964:
    print(f'key={k}: value={v}')

for k,v in thisdict.items():
  if v == 1964:
    print(f'key={k}: value={v}')

print([k for k,v in thisdict.items() if v == 1964])

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
def doesKeyExist(d, k):
  return k in d.keys()
_d1 = { 'name': 'danny', 'age': 20}
print(doesKeyExist( _d1, 'address'))

# def tryAdd(d, k, v)
#   if key exist in dict return False
#   elif key does NOT exists return true and add to dictionary (k:v)
def tryAddIfNotExist(d, k, v):
  if doesKeyExist(d, k):
    return False
  d[k] = v
  return True
_d1 = { 'name': 'danny', 'age': 20}
print('tryAddIfNotExist with age',tryAddIfNotExist( _d1, 'age', 22))
print(_d1)
print('tryAddIfNotExist with address',\
      tryAddIfNotExist( _d1, 'address', 'Tel Aviv'))
print(_d1)

# def tryDelete(d, k)
#   d dictionary k key
#   if key exist in dict delete it and return it
#       if not return None
def tryDelete(d, k):
  if doesKeyExist(d, k):
    return d.pop(k)
  return None
_d1 = {'name': 'danny', 'age': 20}
tryDelete(_d1, 'age')
print(_d1)

# create a dictionary of cities in the world and their population:
#   Tel-aviv, london, paris, tokyo
#    { tel-Aviv: 451520 ,  ... }
#   input a city name from user
#     print the city number of citizens
#     if city does not exist print 'city does not exist in the dict'
#   input a number from the user
#     if there is acity with number of citizens in the dict print the city name
_citizens = { 'tel-Aviv': 451520 , 'paris': 2_140_526, 'tokyo': 14_043_239,
              'london': 8_173_941}

city = input('please enter city name: ')
if doesKeyExist(_citizens, city):
  print(f'in {city} there are {_citizens[city]:,} citizens')
else:
  print(f'city {city} does not exist in dictionary')

# _citizens.setdefault()
population = int(input('please enter num of citizens: '))
print(', '.join([k for k,v in _citizens.items() if v == population]))

# def getSize(d)
#     return the size of the dictionary (number of items)

# def isDictKeysAlpha(d)
#     returns true if all the keys are alpha (hint: use isaplhpa)
# def popByValue(d, v)
#     pop all items with the v specific value
#     return a list of all of the removed items
# def compareDict(d1, d2)
#     return True if all keys+values are similar between dictionaries
# def printDictionary (d)
#  * etgar: use for loop on d.items()