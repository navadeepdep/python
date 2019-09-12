squares = []
for x in range(10): 
    squares.append(x**2)        #add elements square to list by using append
print(squares)

# this will return map object [map(lambda x: x**2, range(10))] hence below code 
#should be used
squares = list(map(lambda x: x**2, range(10))) 
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

#loop thru x and then y 
combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)

#traditional approach
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
           combs.append((x, y))
print(combs)