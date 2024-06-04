import math
# print out the available options ( investment/bond)
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# request the user to enter input and convert it to lower case

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
# check the user's choice and respond accordingly
if user_choice == "investment":
    print("You entered investment.")
elif user_choice ==  "bond":
    print(" you have entered bond")
else:
    print("Invalid choice.Please enter between investment or bond")

# get deposit amount , interest rate, number of years and interest choices
# Create variable for the formula
# Calculate and print out the interest
if input == "investment":
     deposit_amount = float(input("Please enter the amount you would like to deposit."))
     interest_rate = float(input("Please enter the interest rate ( as a percentage)"))
     number_of_years = int(input("Please enter the number of years you plan to invest"))
     interest = input(" Enter either 'simple' or 'compound'  from the menu above to proceed:.").lower()
     if input == 'simple':
      A = deposit_amount * (1 + interest_rate*number_of_years) 
      print("Total amount:",A)
if input=='compund':
      A = deposit_amount * math.pow(1+interest_rate,number_of_years)
      print("Total amount:",A) 
# Create variable for the formula
# Request input and calculate repayment 
if user_choice == "bond":
    i = (interest_rate/100)/12
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate  "))
    number_of_months = int(input("Enter the number of months "))
    repayment = (i * present_value)/(1 - (1 + i)**(-number_of_months))
    print("Total amount:",repayment)






