# Given a year, return the century it is in.

# Define Function
def get_century(year):
    century = (year -1) // 100 + 1
    return century

year = int(input("Enter a year:"))    

century_result = get_century(year)

print(f"The year {year} is in the {century_result} century.")