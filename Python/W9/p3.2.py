password_lookup= {}
while True:
    username = input("enter your username: ")
    if username == 'z':
        break
    password = int(input("enter your password: "))
    password_lookup[username] = password
    print(password_lookup)
