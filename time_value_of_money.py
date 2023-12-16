# The time value of money is a financial concept that recognizes the idea that a sum of money has a different value today compared to its value in the future.
# The principle behind TVM is based on the fact that money can earn interest or have different purchasing power over time.

# The basic TVM formulas involve present value (PV), future value (FV), interest rate (r), and the number of periods (n):
# Present value = FV / (1 + r)^n
# Future value = PV * (1 + R)^n

# where:
# PV is the present value,
# FV is the future value,
# r is the interest rate per period,
# n is the number of periods

# Define the present value function
def calculate_present_value(future_value, interest_rate, period):
    present_value = future_value / (1 + interest_rate) ** period
    return present_value

# Define the future value function
def calculate_future_value(present_value, interest_rate, period):
    future_value = present_value * (1 + interest_rate) ** period
    return future_value

# Ask user for input
future_value_input = float(input("Enter the future value: "))
interest_rate_input = float(input("Enter the interest rate: "))
period_input = float(input("Enter the period: "))

# calculate the present value
present_value_result = calculate_present_value(future_value_input, interest_rate_input, period_input)

print(f"The Present Value is: ${present_value_result:.2f}")

# calculate future value
future_value_result = calculate_future_value(present_value_result, interest_rate_input, period_input)

print(f"The Future Value is: ${future_value_result:.2f}")
