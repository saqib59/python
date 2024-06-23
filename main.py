'''
100 days of code - Python
'''

def calculateGmean(a,b):
    mean = (a*b) / (a+b)
    print(f"mean is {mean}")

    if (a>b):
        print(f"{a} is greater")
    else:
        print(f"{b} is greater")

num1 = 5
num2 = 10
calculateGmean(5,10)