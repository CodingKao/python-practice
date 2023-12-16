# Cash-on-Cash Return is a financial metric used in real estate investing to evaluate the return on actual cash invested in a property.
# It's expressed as a percentage and provides insight into the cash flow performance of an investment relative to the amount of cash initially invested. The formula for calculating Cash-on-Cash Return is as follows:
# Cash-on-cash return = (Net Operating Income / Total Cash Invested) * 100

# define the function
def calculate_cash_on_cash_return(noi, total_cash_invested):
    # calculate cash-on-cash return
    cash_on_cash_return = (noi / total_cash_invested) *100
    return cash_on_cash_return

# ask user for input
noi = float(input("Enter the Net Operating Income: "))
total_cash_invested = float(input("Enter the Total Cash Invested: "))

# calculate the cash-on-cash return
result = calculate_cash_on_cash_return(noi, total_cash_invested)

# print result
print(f"The cash-on-cash return is: {result:.2f}%")