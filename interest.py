# Prompt the user for an Initial Balance (and save to a variable)
# use the float() function to convert the input into a number.
init_bal = float(input("Enter your initial balance: "))

# Prompt the user for an Annual Interest % (and save to a variable)
# use the float() function to convert the input into a number
annual_interest_rate = float(input("What is your annual interest rate (%): "))

# change the percentage number into a decimal (e.g. 6 turns into .06, 5 turns into .05, etc).
# remember to save your new value to a variable!
interest_dec = annual_interest_rate / 100.0

# Prompt the user for a Number of years (and save to a variable)
# use the int() function to convert the input into an integer
years = int(input("Enter the number of years to calculate: "))

# Calculate the total value following the formula.
# You can use multiple steps and variables if necessary.
# Note that n = 12
total_value = round((init_bal * (1 + (interest_dec / 12))**(12*years)),2)

# Calculate the interest earned based on the above value and the initial balance
interest_earned = round(total_value - init_bal,2)

# Output the interest earned
print("Interest earned in "+str(years)+" years: $"+str(interest_earned))

# Output the total value
print("Total value after "+str(years)+" years: $"+str(total_value))
