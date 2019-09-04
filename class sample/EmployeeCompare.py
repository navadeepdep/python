class EmployeeCompare():
    # __init__ used to initialize the instance variables    
    def __init__(self, fname, lname, age, sal):
        print('called during initialization of object')
        self.fname = fname
        self.lname = lname
        self.age = age
        self.sal = sal

    #greater than or equal to   
    def __ge__(self, other):
        return self.age >= other.age
     
    #greater than  
    def __gt__(self, other):
        return self.age > other.age
     
    #less than or equal to   
    def __le__(self, other):
        return self.age <= other.age

    #less than   
    def __lt__(self, other):
        return self.age < other.age
            
    #equal to          
    def __eq__(self, other):
        return self.age == other.age

 
def main():
    # define some employees in a list
    dept = []
    dept.append(EmployeeCompare("Navadeep", "D", 31, 9000))
    dept.append(EmployeeCompare("Ashish", "c", 28, 16000))
    dept.append(EmployeeCompare("Ashish", "S", 28, 10000))
    dept.append(EmployeeCompare("Manoj", "A", 30, 60000))
    dept.append(EmployeeCompare("Swamy", "K", 35, 13000))
    dept.append(EmployeeCompare("Ashish", "D", 28, 10000))


    # determing senior, based on the age 
    print(bool(dept[0] > dept[2]))
    print(dept[1] < dept[3])
  

    # sort the objs using the certeria defined in above functions
    emps = sorted(dept)
    for emp in emps:
        print(emp.fname, emp.lname,  emp.age)


if __name__ == "__main__":
            main()