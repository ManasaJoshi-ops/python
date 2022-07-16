# INPUT FROM THE USER
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# BMI CALCULATOR
BMI=(weight)/(height*height)
print(round(BMI,2))
# CONDITIONAL STATEMENTS
if BMI<18.5 :
  print("You are underweight")
elif BMI>18.5 and BMI<25:
  print("You have normal weight")
elif BMI>25 and BMI<30:
  print("You are slightly overweight")
elif BMI>30 and BMI<35:
  print("You are obese")
elif BMI>35:
  print("You are clinically obese")
