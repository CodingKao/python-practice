# The Gross Rent Multiplier (GRM) is a real estate metric used to evaluate the potential value of an investment property.

# The Gross Rent Multiplier is often used as a quick and rough measure to assess the relative value of different investment properties. A lower GRM generally suggests that the property may be a better value because it indicates a shorter time for the property to pay for itself based on the rental income.

# Define the Gross Rent Multiplier function
def grm(property_price,gross_rental_income):
    # calculate grm
    grm = property_price / gross_rental_income
    return grm


# # Ask user for input
property_price = float(input("Enter a property price: "))
gross_rental_income = float(input("Enter the gross rental income: "))


# # calculate GRM
result = grm(property_price,gross_rental_income)


# Print result
print(f"THe Gross Rent Multiplier (GRM) is: {result:.2f}")