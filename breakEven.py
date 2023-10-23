def calculate_breakeven():
    fixed_costs = float(input("Enter total fixed costs: $"))
    variable_costs = float(input("Enter variable costs per unit: $"))
    selling_price = float(input("Enter selling price per unit: $"))

    if variable_costs <= 0:
        print("Variable costs must be greater than 0.")
    else:
        breakeven_point = fixed_costs / (selling_price - variable_costs)
        print(f"The breakeven point is {breakeven_point:.2f} units.")

if __name__ == "__main__":
    calculate_breakeven()
