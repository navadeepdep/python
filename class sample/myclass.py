class Person:
  def __init__(self, name, cmp):
    self.name = name
    self.cmp = cmp

  def myfunc(self):
    print("Hello my name is " + self.name + " working for " + self.cmp)

p1 = Person("Navadeep", 'EPAM')
p1.myfunc()
 




