# The Loan-to-Value ratio (LTV) is a financial term used in real estate to express the ratio of a loan to the value of an asset being purchased. 

# it's commonly used to assess the risk of a mortgage loan. 
# Loan to Value ratio (LTV) = loan amount / appraised value or purchase price * 100

# Define the LTV ratio function
def loan_to_value_ratio(loan_amount, appraised_value):
    # LTV ratio
    loan_to_value_ratio = loan_amount / appraised_value * 100
    return loan_to_value_ratio


# Ask for user input
loan_amount = float(input("Enter remaning loan amount: "))
appraised_value = float(input("Enter appraised value: "))

# Calculate the LTV ratio
result = loan_to_value_ratio(loan_amount, appraised_value)


# Print Result
print(f"The loan-to-value (LTV) ratio: {result:.2f}%")