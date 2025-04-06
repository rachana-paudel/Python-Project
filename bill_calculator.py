
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




print("welcome to the Bill Calculator")
bill=float(input("What is the total bill?\t"))
bill_tip=int(input("What is the percent of tip you would like to give?\t"))
bill_split=int(input("How many people are going to split the bill?\t"))
tip_amount=(bill_tip/100) * bill
total_bill=bill + tip_amount
bill_per_person=total_bill/bill_split
print(f"Bill per person is : {bill_per_person}")



