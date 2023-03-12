while True:
    num=int(input("enter any number: "))
    if(num>0):
        print("positive number")
    elif(num<0):
        print("negative number")
    else:
        print("neither positive nor negative")
        if(num==0):
            break
