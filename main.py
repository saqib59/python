'''
100 days of code - Python
'''


import datetime;

currentTime = datetime.datetime.now();

if (currentTime.hour >= 6 and currentTime.hour <= 10):
    print("Good morning sahab!")
elif (currentTime.hour >= 11 and currentTime.hour <= 13):
    print("Good afternoon sahab!")
elif (currentTime.hour >= 14 and currentTime.hour <= 19):
    print("Good evening sahab!")
else:
    print("Good night sahab!")
