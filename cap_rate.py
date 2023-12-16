# CAP rate: Measures return on investment in real estate by comparing net operating income to market value.

# Define the function for calculating cap rate
def calculate_cap_rate(noi, current_market_value):
    if current_market_value == 0:
        print("Error:  Cureent Market Value cannot be zero.")

    cap_rate = (noi / current_market_value) * 100

    return cap_rate

noi = float(input("Enter the net operating income (NOI): "))
current_market_value = float(input("Enter the current market value of the property: "))

result = calculate_cap_rate(noi,current_market_value)

print(f"The CAP Rate is: {result:.2f}%")

