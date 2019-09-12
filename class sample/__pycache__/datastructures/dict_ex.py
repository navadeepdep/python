
tel = {'jack': 4098, 'sape': 4139}
tel['nava'] = 5523

t = {x: x**2 for x in (2, 4, 6)}
l = [1, 2, 3]

t1= [(x, y) for x, y in enumerate(l)]
print(t1[1])
print(t)
print(tel)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(q,a)

d = {'a': 1}
h = {'b': 2, **d}
print(h)

a = {**tel}
print(a)

for i in reversed(range(10, 1, -2)):
      print(i)

lis = sorted(((k,x) for k,x in tel.items()), key=lambda item: item[1] )

# print(lis)

# print((1, 2, 3) == (1.0, 2.0, 3.0))

# print(type(1) == type(1.0))


# i=5
# if type(i) != tuple:
#     print('hello')

# h = [ [ k for k in i ]  i if isinstance(i,tuple) else  for i in t  ]

print(isinstance(1,tuple) == False)
kk = [[1,2,3],[3,4],56,[3,5],89]

# z =[**kk]
# print(z)
# l = [[1,4,5], [3,5,6], [4,7,8]]

print(["Even" if i%2==0 else "Odd" for i in range(8)])

string1, string2, string3 = '', '', 'deep'

test = string1 or string2 or string3

print(test)

h = ["hekkk" if 1 != 1 else 'cokkkkk']
t = (1, 2, ('abc', 'a'), 4)

print(h)

#itearting the list of elements in tuple

t = (1, 2, ('abc', 'a'), 4)
for i in t:
    print("------------",i)
    if type(i)==tuple:
       for k in i:
           print("********",k)
