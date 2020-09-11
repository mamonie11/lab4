w = float(input("Enter weight of person in Kgs: "))
h = float(input("Enter height of person in cms: "))
BMI = w/((h/100)**2)
print("BMI of this person is %.1f"%BMI)
if BMI<18.5:
    print("person has underweight")
elif BMI<=24.9 and BMI>=18.5:
    print("person has normal weight")
elif BMI>=25 and BMI<=29.9:
    print("person has overweight")
elif BMI>=30:
    print("person has obesity")