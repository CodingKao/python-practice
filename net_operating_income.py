# Net Operating Income (NOI) is a key financial metric used in real estate to evaluate the profitability of an income-generating property.

# It is calculated by subtracting the property's operating expenses from its total operating income. Here's the formula for calculating Net Operating Income:
# NOI = total operating income - operating expense

# Define the function for calcualting Net Operating Income
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
    total_operating_expense = (
        property_management_fee
        + property_maintenance
        + property_taxes
        + insurance 
        + utilities
        + other_expenses
    )

    noi = total_operating_income - total_operating_expense