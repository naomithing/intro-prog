def get_username():
    """This function prompts the user for their username"""
    username = input("please enter your name")
    return username
def get_password():
    """This function prompts the user for their password"""
    password = input("please enter your password")
    return password
def get_credentials():
    """This function prompts the user for their username and password and returns a tuple containing both values"""
    username = get_username()
    password = get_password()
    return username, password
#call the get_credentials() function and store the returend values in variables
username, password = get_credentials()
print (f"Username: {username}") #f = format
print (f"Password: {password}")

