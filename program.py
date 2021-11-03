# [“apple”, “banana”, “cherry”, “kiwi”, “mango”]
#create a list of all the fruits with the letter ‘a’
# inside them using list comprehension
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
print([one_fruit for one_fruit in fruits if one_fruit.count('a') > 0])
_result = []
for one_fruit in fruits:
    if one_fruit.count('a') > 0:
        _result.append(one_fruit)
print(_result)
print([one_fruit for one_fruit in fruits if one_fruit.find('a') >= 0])
print([one_fruit for one_fruit in fruits if 'a' in one_fruit])

#some_list = [1,4,7,12,19,22, 23, 26].
# create of list of string for even or odd: in this case
# [‘1 is odd’, ‘4 is even’, ‘7 is odd’ …] using list comprehension
some_list = [1,4,7,12,19,22, 23, 26]
#            [expression] if [condition] else [expression]
#            'zugi' if [condition] else 'e-zugi'
print([f'{one_number} is {"zugi" if one_number % 2 == 0 else "e-zugi"}'\
       for one_number in some_list])
print([f'{one_number} is zugi' if one_number % 2 == 0\
           else \
       f'{one_number} is e-zugi'
       for one_number in some_list])
print([(one_number, "zugi" if one_number % 2 == 0 else "e-zugi")\
       for one_number in some_list])

#*etgar: list1 = [1,2] ; list2 = [4,5].
# create a list of tuples [(1,4), (1,5), (2,4), (2, 5)]
# using list comprehension
list1 = [1,2]
list2 = [4,5]
print([(item_list1, item_list2)
       for item_list1 in list1
       for item_list2 in list2])

# demo
counter = 0
for i in range(1, 5): #4
    # -- 4, 4, 4
    # print(i)
    for j in range(1, 6): #5
        print(i, j, end=' ')
        counter += 1
    print()
print('counter=',counter)