class Base1(object): 
    def __init__(self): 
        self.str1 = "Geek1"
        print("Base1")

    def gethere(self):
        print('from base 1')
  
class Base2(object): 
    def __init__(self): 
        self.str2 = "Geek2"        
        print("Base2")

    def gethere(self):
        print('from base 2')
    
    def testme(self):
        print("hello I have been called from testme() !!")

    #def getValue(self):
    #     return "from base2 " + self.str2
  
class Derived(Base1, Base2): 
    def __init__(self): 
          
        # Calling constructors of Base1 
        # and Base2 classes 
        Base1.__init__(self) 
        Base2.__init__(self) 
        print("Derived")

    def gethere(self):
        print('from base derived')
          
    def printStrs(self): 
        print(self.str1, self.str2)
        
        
         
  
ob = Derived() # obje of derived class created
ob.testme() 
ob.gethere() # frist base class method would be invoked 
ob.printStrs() #prints inherited variable values
