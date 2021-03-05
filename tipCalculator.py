#Greeting
print("Can't think of an appropiate tip? We're here to help")

#bill is a float for exact value not includining tip
bill = float(input("Enter Total Bill: "))

print("\n")

#here the amount of guests at dinner is being input
number_of_people = int(input("Total amount of Guests: "))

print("\n")

#percentage_of_tip helps us determine how much guests want to tip
percentage_of_tip = int(input("What percentage of tip would you like to give?"))

#variable represnts sales tax
sales_tax = float(.10)

print("\n")

#use "%.2f" to give only the first two digits after decimal
contributions_per_guest = ("%.2f" % round(float(((percentage_of_tip/100 +1)* bill)/number_of_people),2))

#test to make sure formula works
print(f"Total contribution per guest: ${contributions_per_guest}")

tip_amount = "%.2f" % float(percentage_of_tip/ 100 * bill)

print(f"OverallTip: ${tip_amount}")

#turned variables number_of_people & tip_amount into floats
number_of_people_tipping = float(number_of_people)
tip_amount_new = float(tip_amount)

tip_per_guest = tip_amount_new / number_of_people_tipping

print(f"Tip per person: ${tip_per_guest}")

the_total_bill = bill + tip_amount_new * sales_tax

print(f"The Total Bill(Including Tip): ${the_total_bill}")

