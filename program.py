# x will not be modified
def foo(x = 2):
    x = x + 1
x = 2 # value type
foo(x)
print(x)

# d will be modified!
def add1(d, k, v):
  d[k] = v
d = {1: 'danny'}
add1(d, 2, 'moshe')
print(d)

# l1 will be modified!
def add_list(l1):
  l1.append('add me')
l3 = [1,2,3]
add_list(l3)
print(l3)

# l1 will NOT be modified!
def add_list(l1):
  l1 = []
l3 = [1,2,3]
add_list(l3)
print(l3)