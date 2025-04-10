



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
                    