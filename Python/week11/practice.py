# 1)EXCEPTION WITH CLASS NAME
# a = 3
# b = 0
# try:
#     d = a/b
# except ZeroDivisionError:
#     print("Can not be divided by zero")
#     print("rest of the code block")

#2)EXCEPTION AS AN OBJECT
# a = 3
# b = 0
# try:
#     d = a/b
# except ZeroDivisionError as e:
#     print(e)
#     print("rest of the code block")

#3)MULTIPLE EXCEPTIONS WITH TUPLE
# a = 10
# b = 0
# try:
#     d=a/g
#     print(d)
# except(NameError,ZeroDivisionError)as e:
#     print(e)
#     print("rest of the code block")

#4)MULTIPLE EXCEPTS
# def divide(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("cannot divide by zero")
#     except TypeError:
#         print("both arguments must be numbers")
#     else:
#         print("result is: {result}")
#     finally:
#         print("exiting the function")
# divide(10,2)
# divide(10,"0")
# divide(10,0)

#5)FULL EXAMPLE
# def divide(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("cannot divide by zero")
#     else:
#         print(f"result is:{result}")
#     finally:
#         print("exiting the function")
# divide(10,2)
# divide(10,0)

#exercise1
# def factorial():
#     try:
#         num = int(input("Enter a number: "))
#         factorial = 1
#         for i in range(1, num + 1):
#             factorial *= i
#         print("The factorial of", num, "is", factorial)
#     except ValueError:
#         print("Invalid input. Please enter an integer.")
# factorial()

fileObject = open("C:\\Users\\HP\\OneDrive\\Desktop\\new\\herald.txt", "a")
# for x in fileObject:
#     print(x)
# fileObject.close()
fileObject.write("\n this line will be added")
fileObject.close()
fileObject = open("C:\\Users\\HP\\OneDrive\\Desktop\\new\\herald.txt", "r")
print(fileObject.read())
fileObject = open("C:\\Users\\HP\\OneDrive\\Desktop\\new\\herald.txt", "w")
fileObject.write("\n this line will overwrite the previous line")
fileObject.close()
fileObject = open("C:\\Users\\HP\\OneDrive\\Desktop\\new\\herald.txt", "r")
print(fileObject.read())

