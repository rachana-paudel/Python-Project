
weight=50
height=1.85



bmi=weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
    
elif bmi == 18.5 &  bmi < 25:
    print("Normal Weight")

elif bmi >= 25:
    print("Overweight")
