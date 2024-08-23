## Max number

number1 = int(input("Enter the number1:-"))
number2 = int(input("Enter the number2:-"))
number3 = int(input("Enter the number3:-"))
number4 = int(input("Enter the number4:-"))

if number1 >= number2 and number1 >= number3 and number1 >= number4:
    print("max value:-", number1)
elif number2 >= number1 and number2 >= number3 and number2 >= number4:
    print("max value:-", number2)
elif number3 >= number1 and number3 >= number2 and number3 >= number4:
    print("max value:-", number3)
else:
    print("max value:-", number4)

results = max(number1, number2, number3, number4)
print(results)
