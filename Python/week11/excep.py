try:
    value = input ("enter a value: ")
    if value == "":
        raise EOFError
except EOFError:
    print("an EOFError occured.")
