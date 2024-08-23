## Grade program
# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

score = int(input("enter the score:-\n"))

if score >= 90 and score <=100:
    print("Your grade is A")
elif score >= 80 and score <=89:
    print("Your grade is B")
elif score >= 70 and score <=79:
    print("Your grade is C")
elif score >= 60 and score <=69:
    print("Your grade is D")
elif score >= 50 and score <=59:
    print("Your grade is E")
elif score >=101:
    print(" you have entered the wrong score,\n score value will be 1 to 100")
else:
    print("Your are fail")