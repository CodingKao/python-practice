# Display invoice to customer

# Ask for customer name
name = input("Enter customer name: ")

# Write a function
def display_invoice(name, amount, due_date):
    print(f"Hi {name}.")
    print(f"Your bill of ${amount:.2f} is due on {due_date}")

display_invoice(name, 50.00, "10/10/2023")