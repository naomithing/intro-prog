while True:
    #get a character input from the user
  char = input ("enter a character: ")
    # use the ord function to get the ASCII value of the character
  char_value =ord(char)
    #increasing the ASCII value by 1 tp get the value of the next character
  next_char_value = char_value + 1
    #use the chr function to convert the ASCII value back into a character
  next_char = chr(next_char_value)
    #print the result
  print(f"the next character after '{char}' is '{next_char}'.")
    # asking user if they want to continue or not
  choice = input("do you want to continue, (Y/N)?")
  if choice.upper() != "Y":
      break #break statement is used to stop or terminate the code
