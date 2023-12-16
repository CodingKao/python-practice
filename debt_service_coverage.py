# The Debt Service Coverage Ratio (DSCR) is a crucial financial metric used by lenders to evaluate a property's ability to cover its debt obligations.
# Debt service coverage ratio = net operating income (NOI) / Debt service (mortgage payment)

# Define the debt service coverage ratio funtion
def calculate_dscr(noi,debt_service):
    # calculate DSCR
    dscr = noi / debt_service
    return dscr

# Ask user for input
noi = float(input("Enter the net operating income (NOI): "))
debt_service = float(input("Enter the debt service (mortgage payment: "))

# calculate DSCR
result = calculate_dscr(noi,debt_service)

# Print result
print(f"The debt service coverage ratio (DSCR) is: {result:.2f})")

                           
