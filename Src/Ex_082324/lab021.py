from pickletools import float8

number1 = float(input("Enter the number1:-"))
number2 = float(input("Enter the number2:-"))
number3 = float(input("Enter the number3:-"))
number4 = float(input("Enter the number4:-"))

if number1 <= number2 and number1 <= number3 and number1 <= number4:
    print(f"min value:- {number1:.2f}")
elif number2 <= number1 and number2 <= number3 and number2 <= number4:
    print(f"min value:- {number2:.2f}")
elif number3 <= number1 and number3 <= number2 and number3 <= number4:
    print(f"min value:- {number3:.2f}")
else:
    print(f"min value:- {number4:.2f}")

results = min(number1, number2, number3, number4)
print(results)