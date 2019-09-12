# import 
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


#comphersion inside a comphersion
mappedRows = [[row[i] for row in matrix] for i in range(4)]
print(mappedRows)


mappedRows = [row[i] for row in matrix for i in range(4)]
print(mappedRows)


#line by line for loop
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

#single line 
print(list(zip(*matrix)))

li = [0.34, 1.23, 66.25, 333, 333, 1234.5]
del li[2:4]
print(li)

# li = [1, 2, 3, 4]
# a ='hello','test', 'hell', 'test12'
# d = {1:2, 2:3, 3:4, 4:5}

# k, b, *c = d.items()
# print(k, b, c)
# print(a, a[0], str(len(a)))

# b = tuple(li)
# print(b)