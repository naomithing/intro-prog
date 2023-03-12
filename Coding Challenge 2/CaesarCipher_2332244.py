#Name: Naomi Thing
#Student ID: np03cs4a220491
def welcome(): #prints the welcome message
    print("Welcome to the Caesar Cipher.")
    print("This program encrypts and decrypts the text with Caesar Cipher.")


def enc(msg,key): #encrypts the plain text
       return "".join([chr((ord(char) + key - 65) % 26 + 65) for char in msg.upper()])

def dec(msg,key):#decrypts the plain text
    return "".join([chr((ord(char) - key - 65) % 26 + 65) for char in msg.upper()])
def text():
     valid_input = False
     while not valid_input:
        mode=input("Would you like to Encrypt (e) or Decrypt (d)? choose 'e' or 'd': ")
        if mode not in ['e','d']:
            print("Invalid input. Please enter either 'e' or 'd': ")
        else:
            valid_input = True
     msg=input("enter the message you would like to encrypt or decrypt: ")
     key=int(input("enter how many times you would like to shift: "))
     if (mode == 'e'):
         encrypt_message = enc(msg, key)
         print(encrypt_message)
     elif (mode == 'd'):
         decrypt_message = dec(msg, key)
         print(decrypt_message)

def reassigned(): #run the program from start if oyu want to continue
    ask = input("Would you like to encrypt or decrypt another message? (Y/N)?: ")
    if (ask == 'y' or ask == 'Y'):
        main()
    elif (ask == 'n' or ask == 'N'):
        print("Thank you for your time.")

def main():
    welcome()
    text()
    reassigned()

main()