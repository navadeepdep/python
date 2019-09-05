import collections
import string


def main():

    text = " Navadeep How are you doing "
    # initialize a deque with lowercase letters
    d = collections.deque(text.lower())

    print("Items: " + str(d), end=" ")
    print(end="-")
    print("'to test end'")

    # deques support the len() function
    print("Item count: " + str(len(d)))

    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end=",")

    # manipulate items from either end
    d.pop() #removes the first element from right
    d.popleft() #removes the first element from left

    print(d)
    
    d.append(2) # appends 2 to the right
    d.appendleft(1) #append to left 
    print(d)

    # rotate the deque
       d.rotate(6) #rotate by 6 characters
    
if __name__ == "__main__":
    main()
