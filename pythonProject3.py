#Tip Calculator:
print("Welcome to the Tip Calculator:")

bill=float(input("What was the total bill in rupees? "))
tip_in_percent=int(input("How much tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))

tip_amount=(tip_in_percent/100)*bill
total_bill=tip_amount+bill
each_person=total_bill/people
each_person_pays=round(each_person,2)

print(f"Each Person should pay :{each_person_pays}")