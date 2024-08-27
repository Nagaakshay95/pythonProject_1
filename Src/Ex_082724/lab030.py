#match statement
user_type = input("Enter the user type, admin, manager, guest\n")# input
user_type = user_type.lower()
match user_type:
    case "admin" | "manager": ## in the match statement for or we should use like |
        print("Hello Sir") ## if you want to use and statement the use if statement logic
    case "guest":
        print("Hello, Guest")
    case _:
        print("Hello, There!")