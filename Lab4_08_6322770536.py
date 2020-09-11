day = int(input("Input number of days: "))
hour = int(input("Input number of hours: "))
print("Please select a choice: ")
print("1-to calculate the total number of seconds or \n2-to calculate the total number of minutes:")
ch = int(input("Enter your selected a choice: "))
if  ch==1:
    x = (day*24*60*60)+(hour*60*60)
    print("--------------------------------------------")
    print("The total number of seconds are",x)
elif ch==2:
    x = (day*24*60)+(hour*60)
    print("--------------------------------------------")
    print("The total number of minutes are",x)
        