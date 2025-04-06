# print("Welcome to the rollercoaster!")
# height=int(input("What is your height in cm?\t"))
# bill=0
# if height>=120:
#     print("You can ride the rollarcoaster?\t")
#     age=int(input("what is your age:\t"))
#     if age<=12:
#         bill=5
#         print("Please pay $5")
#     elif age <=18:
#         bill=10
#         print("Pease pay $5")
#     elif age >= 45 and age <= 55:
#         print("Everthing is going o be ok")
#     else:
#         print("Please pay $10")

#     want_photos=input("Do you want photos? type u for yes and n for no\t")
#     if want_photos=="y":
#         bill += 3
        
#     print(f"Your final bill is {bill}")    

# else:
#     print("Sorry you cannot ride rollarcoaster.")                





########################################Pizza choices########################################

print("Welcome to foodland!!")
bill=0
size=input("What size pizza do you want? 'S, 'M','L': ")

if size == "S":
    bill += 5
elif size=="M":
    bill += 10
elif size =="L":
    bill += 15

else:
    print("You have entered the invalid input.")



chilli_flakes=input("Do you want chilli_flakes on your pizza? Y or N:")

if chilli_flakes=="Y":
    bill += 5
elif chilli_flakes=="N":
    bill += 0

else:
    print("You have entered invalid input.")
    
extra_cheese=input("Do you want extra cheese? Y or N: ")
if extra_cheese=="Y":
    bill += 10
elif extra_cheese=="N":
    bill += 0
else:
    print("You have entered invalid input.")      


print(f"You total cost will be {bill}")
                    