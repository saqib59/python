'''
100 days of code - Python
'''

# you can not have a default argument followed by a non default arguement
# def average(a,b=3):
#     print(f"a = {a} & b = {b}")

# average(2,4)

def average(*numbers):
    sum = 0
    for item in numbers:
        sum = sum + item

    return sum / len(numbers)

test = average(2,2,2)

print(test)