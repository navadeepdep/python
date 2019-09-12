class A: 
    #   k = 0
      def __init__(self, k, n = 'Rahul'): 
              self.k = k
              self.name = n 
              print("from baseA: ")
      print("hello from baseA: ")

      def greet(self, msg):
         print("from greet ...", msg) 
       
class B(A): 
      def __init__(self, roll, k): 
              self.roll = roll
              print("from baseB: ")
            
      def greet(self, m):
          print("derived greet() calling the base class A greet() using super keyword")
          super().greet(m)
      
      
  
object = B(23, 456) 
object.greet("Hello Navadeep")

# print (object.k)
# print (object.name)