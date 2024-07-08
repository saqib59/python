#Grade calculator

user_marks = 50

if user_marks not in range(50, 101):
    print("Please verify your marks again")
    exit()

if user_marks >= 90 :
    print("user has A grade")
elif user_marks >= 80 :
    print("user has B grade")
elif user_marks >= 70 :
    print("user has C grade")
elif user_marks >= 60 :
    print("user has D grade")
else:
    print("user has failed")