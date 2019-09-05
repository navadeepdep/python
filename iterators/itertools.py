import itertools


def testFunction(x):
    return x < 40


def main():
    
    #Python object that implements the .__iter__() or .__getitem__() methods is iterable.

    # cycle iterator can be used to cycle over a collection
    seq = ["hello", "first", "program"]
    c = itertools.cycle(seq)
    #range takes 3 inputs first is start index, second is end index and their is for increment of index by
    for i in range (1, 10, 2) :
        print(next(c))

    #range of values print in reverse order
    for i in range (20, 1, -2) :
        print("value is: ", i)


    # use count to create a simple counter
    count1 = itertools.count(100, 10)
    for i in range(3):
        print(next(count1))

    # accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    acc = itertools.accumulate(vals, max)
    print(acc)
    print(list(acc))

    str1 = "hello is word"
    print(str1.isalpha())
        
    # use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))
    
    # dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print("using the dropwhile()")
    print(list(itertools.dropwhile(testFunction, vals)))
    print("using the takewhile()")
    print(list(itertools.takewhile(testFunction, vals)))
    
    
if __name__ == "__main__":
    main()
    