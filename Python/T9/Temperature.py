def temperature():
    t = float(input("enter the temperature in celsius "))
    if (t<=37):
        print("they have low temperature")
    elif (t>=37):
        print("they have fever")
    else:
        print("they have normal temperature")

temperature()