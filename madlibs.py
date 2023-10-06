#display welcome message
print("Welcome!  Please enter your address:")

# 1.1 Ask the user to enter a mailing address: street, city, state, zipcode
# collect address fields (variables)
street = input("Street number: ")
city = input("Enter City: ")
state = input("Enter State: ")
zip_code = input("Zip: ")

#1.2 Using string methods, ensure that the address will be properly capitalized, no matter how it's entered.
street = street.title()
city = city.title()
state = state.title()

# format address using f-string
print(f'''
{street}
{city}, {state}
{zip_code}
''')



#mad libs self-introduction
'''Hi.  My name is "".  I am "" years old.  I am from "". 
In my spare time I like to "" and "".  My favorite color is ""
and my favorite number is "".  My dream is to be a "".'''

#variables
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter city you are from: ")
activity_1 = input("Enter activity you like to do for fun: ")
activity_2 = input("Enter activity you like to do for fun: ")
fav_color =input("Enter your favorite color: ")
fav_number = input("Enter your favorite number: ")
occupation = input("Enter your dream occupation: ")

print(f"""Hi.  My name is {name}.  I am {age} years old.  I am from {city}. In my spare time I like to {activity_1} and {activity_2}. My favorite color is {fav_color}
,my favorite number is {fav_number}.  My dream is to be a {occupation}.""")