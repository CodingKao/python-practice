# Net Operating Income Calculator

# Write a code that calculates the Net Operating Income (NOI) based on user input

print("=== Net Operating Income (NOI) Caculator ===")

# Get User input
gross_income = float(input("Enter total gross rental income ($): "))
operating_expenses = float(input("Enter total opearting expenses ($): "))

# Calculate NOI
noi = gross_income - operating_expenses

# print result
print("\nNet Opearting Income (NOI):  $" + str(round(noi,2)))
