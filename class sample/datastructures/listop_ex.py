
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
#count item in a list
print(fruits.count('apple'))

print(fruits.count('tangerine'))

#Find index in a list
print(fruits.index('banana'))
# Find next banana starting a position 4
print(fruits.index('banana', 4))  

#Reverse the list
fruits.reverse()
print(fruits)

#Add an element to the list
fruits.append('grape')
print(fruits)

#Sort the list
fruits.sort()
print(fruits)

#Pop an element from the list
fruits.pop()
print(fruits)