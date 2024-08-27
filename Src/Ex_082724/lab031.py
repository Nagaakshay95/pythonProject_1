value = int(input("enter the value\n"))

match value:
    case x if x % 2 == 0 and x > 10: # so we are combining with two condition
        print("the number which is enter is even and grater than 10")
    case _:
        print("enter value is not match with the condition")
