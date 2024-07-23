factorial = 6
result = 1

while factorial > 1:
    result *= factorial
    factorial -= 1

print(result)  # This will correctly print 720, which is 6!
