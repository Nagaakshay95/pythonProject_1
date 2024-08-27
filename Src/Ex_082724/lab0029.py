#match statement
# match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block
# simple understanding it is used as if else statement
# Write a program to ask the user which browser he want to run automation
browser_name = input("Enter the name of the browser\n")## we getting input from user
browser_name = browser_name.lower() ## it is used for lower case or uppercase sensitive
match browser_name:##if browser name is match enter into the statement or else go to the (_)default statement
    case "firefox":
        if browser_name == "firefox":
            print("Hello Hello")
        print("Excute the firefox Code")
    case "chrome":
        print("Excute the Chrome Code")
    case "edge":
        print("Excute the Edge Code")
    case "safari":
        print("Excute the Safari Code")
    case _:## _ means default statement
        print("Browser Not Found!")