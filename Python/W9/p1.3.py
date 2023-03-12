def temp_humi():
    temperature=int(input("enter the temperature: "))
    humidity=int(input("enter the humidity: "))
    if (temperature >= 85 and humidity > 60 ):
        print ('muggy day today')
    elif (temperature >= 85):
        print('warm, but not muggy today')
    elif(temperature >= 65):
        print('pleasant today')
    elif(temperature <= 45):
        print('cold today')
    else:
        print('cool today')
temp_humi()
