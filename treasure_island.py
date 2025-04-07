print("Welcome to Treasure Island.")
choice=input("Do you want to go left or right? type left or right\t")

if choice=="left":
    choice2=input("Do you want to swim or wait. Type swim or wait.\t")


    if choice2=="swim":
        print("Game Over")
    elif choice2=="wait":
        choice3=input("Which door you want to enter? Red, Yellow or Blue\t")
        if choice3=="Red":
            print("Game OVer")
        elif choice3=="Blue":
            print("Game Over.")
        else:
            print("You won!!")   
    else:
        print("You have entered wrong input.")         
            
else:
    print("Game Over.")            
