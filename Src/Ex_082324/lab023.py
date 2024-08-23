#simplfiled chain

score = int(input("enter the score:-\n"))

if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score <= 89:
    print("Your grade is B")
elif 70 <= score <= 79:
    print("Your grade is C")
elif 60 <= score <= 69:
    print("Your grade is D")
elif 50 <= score <= 59:
    print("Your grade is E")
elif score >=101:
    print(" you have entered the wrong score,\n score value will be 1 to 100")
else:
    print("Your are fail")