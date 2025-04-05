# print("Hello" + input("What is your name?") + "! ")

# name=input("What is your name?")
# print(len(name))


# print(len(input("What is your name?")))

# username=input("What is your name?")
# length=len(username)
# print(length)

# print("Welcome to the Band Name Generator.")
# a=input("What's the name of the city you born?\n")
# b=input("What's your pet name?\n")
# print("Your band name could be" " "+ a + " " +b)

# print("hello" [1])
# print(type(111))

# name_of_user=input("Write your name:\n")
# length_of_name=len(name_of_user)

# print(name_of_user + " "+ str(length_of_name))//this is not accepeted as we can't concatenate int to str

# print(name_of_user + " "+ str(length_of_name))
# print("My age:" + str(12))

# print(123+456)
# print(9-8)
# print(3*2)
# print(6/3)
# print(4/3)
# print(4//3)
# print(int(4/3))
# print(2**4) #**act as power

# bmi=84/1.65 ** 2
# print(bmi)
# print(int(bmi))
# print(round(bmi))
# print(round(3.5))

# age=5
# print(f"Your age will be {age+1} next year") #f string will not print {} beacket rather print value inside bracket like age=5+1=6


# print("Welcome to the print calcultor")
# bill= float(input("What was the total bill? $"))
# tip=int(input("What percentage tip would you like to give? 10 12 15\t"))
# people=int(input("How many people to split the bill?"))
# tip_as_percent=tip/100
# total_tip_amount=bill * tip_as_percent
# total_bill=bill + total_tip_amount
# bill_per_person=total_bill/people
# final_amount=round(bill_per_person,2)
# print(f"Each person should pay:${final_amount}")



# print("Welcome to the bill calculator")
# bill=float(input("What was the total bill?\n"))
# tip=int(input("What is the percentage of tip you would like to give?\t"))
# bill_split=int(input("How many people will split the bill?\n"))
# tip_as_percent=(bill / 100) * bill
# total_bill=tip + tip_as_percent
# bill_per_person=total_bill/bill_split
# print(f"Bill per person is {bill_per_person}")


print("welcome to the Bill Calculator")
bill=float(input("What is the total bill?\t"))
bill_tip=int(input("What is the percent of tip you would like to give?\t"))
bill_split=int(input("How many people are going to split the bill?\t"))
tip_amount=(bill_tip/100) * bill
total_bill=bill + tip_amount
bill_per_person=total_bill/bill_split
print(f"Bill per person is : {bill_per_person}")

