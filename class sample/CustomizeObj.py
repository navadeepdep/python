# customize string representations of objects


class Employee():
    def __init__(self):
        self.fname = "Navadeep"
        self.lname = "D"
        self.age = 30

    # use __repr__ to create a string useful for debugging
    def __repr__(self):
        return "<Employee Class - fname:{0}, lname:{1}, age{2}>".format(self.fname, self.lname, self.age)

    # use str for a more human-readable string
    def __str__(self):
        return "Employee ({0} {1} is {2})".format(self.fname, self.lname, self.age)

    # use bytes to convert the informal string to a bytes object
    def __bytes__(self):
        val = "Employee:{0}:{1}:{2}".format(self.fname, self.lname, self.age)
        return bytes(val.encode('utf-8'))


def main():
    # create a new Person object
    cls1 = Employee()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    i=8
    print("Calculation is performed here  {:6d} {:6d} {:6d} {:6d}".format(i, i ** 2, i ** 3, i ** 4)) 

    print("{:d}{:d}".format(1, 2))
    print("Formatted: {0}".format(cls1))
    print(bytes(cls1))


if __name__ == "__main__":
    main()
