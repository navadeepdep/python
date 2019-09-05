# use transform functions like sorted, filter, map

def myfilter(k):
    if k.islower():
        return k.upper()
    return k.lower()

def onlylower(k):
    if k.islower():
        return True
    return False

def performFunc(x):
    if x%2 ==0:
        return x**2
    return x**3

def main():
   
    test = ['K', 'a', 'S', 'z', 'E', 'Q', 'n', 'C', 'h', 'M', 'd']
    nums = [1,2,3,4,5,6]

    opchar = list(map(myfilter, test))
    sopchar = sorted(opchar, key=opchar.index, reverse=True)
    print("sopchar: " , sopchar)

    olower = list(filter(onlylower, test))
    print("only lowercase letters are printed :", olower )    

    # use map to create a new sequence of values
    squares = list(map(performFunc, nums))
    print(squares)

if __name__ == "__main__":
    main()
