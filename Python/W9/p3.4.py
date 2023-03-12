password_hint={"gmail.com": 2222}
username = input("what is the email address?")
if username == "gmail.com":
    print("Welcome.")
else:
    print("invalid!!!")
    password=int(input("enter the password: "))
    if (password == 2222):
        print("correct password")
    else:
        print("incorrect password")
        if(username == "gmail.com" and password == 2222):
            password_hint[username]=password
            print(password_hint)
        else:
            print("5 mins till you can try again")

