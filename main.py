'''
100 days of code - Python
'''


number = int(input("Enter the value of x: "))

match (number):
    case (3):
        print("number is 3")
    case (5):
        print("number is 5")
    case _ if number!=90:
       print(f"{number} is not 90")
    case _ if number!=80:
       print(f"{number} is not 80")
    case _:
       print(number)
