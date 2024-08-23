##Task 5
# compare number with if else conditions

number1 = int(input("Enter the number1:-"))
number2 = int(input("Enter the number2:-"))
number3 = int(input("Enter the number3:-"))
number4 = int(input("Enter the number4:-"))

if number1 >= number2 and number1 >= number3 and number1 >= number4:
    print(number1)
elif number2 >= number1 and number2 >= number3 and number2 >= number4:
    print(number2)
elif number3 >= number1 and number3 >= number2 and number3 >= number4:
    print(number3)
elif number4 >= number1 and number4 >= number2 and number4 >= number3:
    print(number4)
else:
    print("Please enter the correct number")



