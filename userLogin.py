# Usher Login

# Define a funciton called 'login' which will have three parameters:
def login(username_attempt, password_attempt, profile):

    if username_attempt == profile['username'] and password_attempt == profile['password']:
        #print('Correct password')
        #print('Successful login.  Welcome!')
        return True

    else:
        #print('Error! Your username or password was incorrect!')
        return False

# Create a dictionary called 'profile'
profile = {
    'username': 'name1', 
    'password': 'password1'
}

# Create a REPL which allows a user to 'log in'

while True:
    # welcome the user
    print('WELCOME! PLEASE LOGIN.')

    # ask for user input
    username_attempt = input('Enter your username: ')
    password_attempt = input('Enter your password: ')

    if login(username_attempt, password_attempt, profile):
        print('Correct password')
        print('Successful login.  Welcome!')
        break

    else:
        print('Error! Your username or password was incorrect!')
   
        # ask user if they want to try again
        again = input('Do you want to try again? y/n: ')
        
        # if user input no (or 'n') end loop
        if again == 'n':
            print('Goodbye!')
            break