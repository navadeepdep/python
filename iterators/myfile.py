from collections import Counter
def test():
    data1 = [2,3,5,6,7]
    str1 = "navadeep"
    data = ['a', 'g', 's', 'f', 'j', 'd', 's', 'e']

    data1.append(str1)
    print(data1)

    d1 = [5,3,5,8,9]

    d1.extend(str1)
    print("from d1", d1)

    d1 = [5,3,5,8,9]

    #print(d1.append(data1))
       
    data1.append(data) 
    print("data1", data1)
    data1 = [2,3,5,6,7]
    data1.extend(data)

    print()

    for i in [*'abc']:
        print("this is from l;oop", i)

   # data2 = data1.update(data)
    print("data1", data1)
    #print("data1", data2)

    myvalue ="navadeep"
    print("counter:",  Counter(myvalue))
    testl = list(myvalue)

    print(testl)
    
    for i in testl:
        print(i)


    s = "mystring"
    l = list(s)
    print(l)


    #print(list(split(myvalue)))
    return [i for i in data if data.count(i) > 1]

def main():
    print("Results:", test())

if __name__ == "__main__": main()

