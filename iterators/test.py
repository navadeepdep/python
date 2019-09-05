def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "navadeep"]


    # use regular interation over the days
    print("printing using range():")
    for m in range(len(days)):
        print(m+1, days[m])

    # using enumerate reduces code and provides a counter
    print("printing using enumerate():")
    for i, m in enumerate(days, start=1):
        print(i, m)

    # use zip to combine sequences
    print("printing elements formed by using zip():")
    for m in zip(days, daysFr):
        print(m)

    # use enumeration to loop thru zip to combine sequences  
    print("enumeration used to loop thru zip elements ")
    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, "-", m[0], "(in English) =", m[1], "(in French)")


    print(type(zip))




if __name__ == "__main__":
    main()