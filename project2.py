#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number.Either round off to 2 decimal places [round(bill_per_person, 2)] or using "{:>2f}".format( ) 

print("Welcome to the tip calculator!")
bill=float(input("what is the total bill?\n"))
tip=int(input("how much tip wouldyou like to give? 10, 12, or 15\n"))
people=int(input("how many people are going to split this bill?\n"))
tip_percent=tip/100
total_tip=bill*tip_percent
total_bill=bill+total_tip
bill_per_person=total_bill/people
final_amount="{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")


#OUTPUT:
#Welcome to the tip calculator!
#what is the total bill?
#150
#how much tip wouldyou like to give? 10, 12, or 15
#12
#how many people are going to split this bill?
#5
#tip_percent=12/100
#tip_percent=0.12
#total_tip=150*0.12
#total_tip=18
#total_bill=150+18
#total_bill=168
#bill_per_person=168/5
#bill_per_person=33.6
#final amount=33.60 (rounding off to 2 decimal places) using "{:.2f}".format(bill_per_person)
#then use f string to concatenate in print function
#Each person should pay: $33.60