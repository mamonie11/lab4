print("Date Formatter")
print("This program asks fot the date as three numbers and formats it correctly")

year = int(input("Please enter the year (YYYY) : "))
month = input("Please enter the month (MM) : ")
if month == "01":
    month = 'January'
elif month == "02":
    month = 'Febuary'
elif month == "03":
    month = 'March'
elif month == "04":
    month = 'April'
elif month == "05":
    month = 'May'
elif month == "06":
    month = 'June'
elif month == "07":
    month = 'July'
elif month == "08":
    month = 'August'
elif month == "09":
    month = 'September'
elif month == "10":
    month = 'October'
elif month == "11":
    month = 'November'
elif month == "12":
    month = 'December'

day = int(input("Please enter the day (DD) : "))
date = ""
if day == 1:
    date = "st"
elif day == 2:
    date = "nd"
elif day == 3:
    date = "rd"
    

print("The date is %d%s %s %d." %(day,date,month,year))