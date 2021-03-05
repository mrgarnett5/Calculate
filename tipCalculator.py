#Greeting
print("Can't think of an appropiate tip? We're here to help")

bill = float(input("Enter Total Bill: "))

print("\n")

number_of_people = int(input("Total amount of Guests: "))

print("\n")

percentage_of_tip = int(input("What percentage of tip would you like to give?"))

print("\n")

contributions_per_guest = ("%.2f" % round(float(((percentage_of_tip/100 +1)* bill)/number_of_people),2))

#test to make sure it works
print(f"Total contribution per guest: ${contributions_per_guest}")


