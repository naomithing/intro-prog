sum=0
for i in range(100):
    num = int (input("enter a positive integer(enter neg num to terminate): "))
    if (num<0):
        break
    elif (num>100):
        continue
    sum += num
    print("the sum of the integers entered is: ", sum)
