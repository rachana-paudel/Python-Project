print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm?\t"))
bill=0
if height>=120:
    print("You can ride the rollarcoaster?\t")
    age=int(input("what is your age:\t"))
    if age<=12:
        bill=5
        print("Please pay $5")
    elif age <=18:
        bill=10
        print("Pease pay $5")
    elif age >= 45 and age <= 55:
        print("Everthing is going o be ok")
    else:
        print("Please pay $10")

    want_photos=input("Do you want photos? type y for yes and n for no\t")
    if want_photos=="y":
        bill += 3
        
    print(f"Your final bill is {bill}")    

else:
    print("Sorry you cannot ride rollarcoaster.")                

