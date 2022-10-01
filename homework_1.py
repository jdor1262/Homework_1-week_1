#Body Mass Index Calculator

print("\n","*"*5,"Body Mass Index Calculator","*"*5)

print("\n\
- Below 18,5: UNDERWEIGHT\n\
- Between 18,5-25: NORMAL\n\
- Between 25-30: OVERWEIGHT\n\
- Between 30-35: OBESE\n\
- Over 35: EXTREMELY OBESE ", "\n")
wgt = float(input("Please in your Weight in 'Kg': "))
print()
hgt = float(input("Please in your height 'cm' : "))
imc = round((wgt / (((hgt/100)**2))),3)
print()
print("Your BMI is: ",(imc))
if imc < 19 :
    print("You are UNDERWEIGHT")
elif imc > 18 and imc < 25:
    print("You are NORMAL")
elif imc > 24 and imc < 30:
    print("You are OVERWEIGHTL")
elif imc > 29 and imc < 35:
    print("You are OBESE")
elif imc > 35 :
    print("You are EXTREMELY OBESE")