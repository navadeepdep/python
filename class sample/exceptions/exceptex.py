try:
    10 * (1/0)    
except ZeroDivisionError as e:
    print(e)

try:
    hello
except NameError as e:
    print(e)

try:
    '2' + 278

except TypeError as e:
    print(e)

def trythis():
    try:
        10*(3/0)
        "2" + 67
        hello
    except (ZeroDivisionError, NameError, TypeError) as e:     
       print(e)
       raise NameError("Zero division is not possible !!")

def handler():
    try:
       trythis()
    except NameError as e:
        print(e)

handler()

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         print(x)
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again    ")

