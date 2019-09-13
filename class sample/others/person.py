class Person:
  def __init__(self, name, cmp):
    self.name = name
    self.cmp = cmp

  def myfunc(self):
    print("Hello my name is " + self.name + " working for " + self.cmp)

  def sendmsg(self):
     print("hello how are you !!")


def main():   
    p1 = Person("Navadeep", 'EPAM')
    p1.myfunc()

if __name__ == '__main__': main()
 