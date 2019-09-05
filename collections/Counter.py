# Demonstrate the usage of Counter objects

from collections import Counter


def main():
    # list of students in class 1
    class1 = ["navadeep", "Bob", "James", "Chad", "Darcy", "Penny", "Hannah"
              "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    #list of studetns in class3
    class3 =["navadeep", "ashish", "manoj", "deep", "navadeep"]

    # Create a Counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)
    c3 = Counter(class3)

    c1.update(class3)
    #print(c1.values())
    print("{:d} total no.of students in class1 after merger with class3" .format(sum(c1.values())))

    c1.subtract(class3)
    print(c1)

    # How many students in class 1 named James?
    print("{:d}  students are in class 1 named James".format(c1["James"]))

    # How many students are in class 1?
    print(sum(c1.values()), "students in class 1")

    # Combine the two classes
    c1.update(class2)
    print(sum(c1.values()), "students in class 1 and 2")

    # What's the most common name in the two classes?
    print(c1.most_common(3))

    # Separate the classes again
    c1.subtract(class2)
    print(c1.most_common(1))

    # What's common between the two classes?
    print(c1 & c2)

    print( )


if __name__ == "__main__":
    main()
