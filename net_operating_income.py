# Define the function for calculating Net Operating Income
def calculate_noi():
    # Get user input for Total Operating Income
    rental_income = float(input("Enter Rental Income: "))
    other_income = float(input("Enter Other Income: "))
    total_operating_income = rental_income + other_income

    # Get user input for Total Operating Expense
    property_management_fee = float(input("Enter Property Management Fee: "))
    property_maintenance = float(input("Enter Property Maintenance: "))
    property_taxes = float(input("Enter Property Taxes: "))
    insurance = float(input("Enter Insurance: "))
    utilities = float(input("Enter Utilities: "))
    other_expenses = float(input("Enter Other Expenses: "))
    total_operating_expenses = (
        property_management_fee
        + property_maintenance
        + property_taxes
        + insurance
        + utilities
        + other_expenses
    )

    # Calculate Net Operating Income (NOI)
    noi = total_operating_income - total_operating_expenses

    # Display result
    print("\nNet Operating Income (NOI): $ {:.2f}".format(noi))

# Call the function to calculate NOI
calculate_noi()