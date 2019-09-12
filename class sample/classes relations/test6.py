class C(object): 
       def __init__(self, e): 
              self.c = 21
  
              # d is private instance variable  
              self.__d = 42
              self.e=e

       def getValue(self):
            print('value of d : ', self.__d)
            return self.__d

class D(C): 
       def __init__(self): 
              self.e = 84
              C.__init__(self, self.e) 
                   


object1 = D()
obj = C(10)

print("getting e value : " , obj.e)
print("getting e value from object1: " , object1.e)

print(obj.getValue())
  
# produces an error as d is private instance variable 
#print(object1.d)
#but can access the other members 
print(object1.c)   