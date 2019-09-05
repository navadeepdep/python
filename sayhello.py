def message():
    print("say hello ....")
    names = ["Michele", "Robin", "Sara", "Michele", "Navadeep"]

    print(names[1:])
    print([a for i, a in enumerate(names) if names[:i]])

    # for i in names:
    #     d.append(i, i)

    # print(d)


 

   


if __name__ == "__main__":
    message()