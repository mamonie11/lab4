print("Welcome to ITS100!")
ID = int(input("Enter student ID: "))
fname = input("Enter first name: ")
lname = input("Enter last name: ")
code = input("Enter register code: ")
if code == "ITS100-2015":
    print("Successful register!")
    print("User information:")
    print("ID: %d"%ID)
    print("Name: %s %s"%(fname,lname))
else:
    print("Fail to register!")