num=input("enter a number: ")
num=int(num)
if(num%5==0 and num%3==0):
    print ("fizzbuzz")
elif (num/3 and num%3==0):
    print("fizz")
elif (num/5 and num%5==0):
    print("buzz")
else:
    print ("invalid")
