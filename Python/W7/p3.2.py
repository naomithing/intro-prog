def addition(n1, n2):
    return round(n1+n2, 2)
def subtraction(n1, n2):
    return round(n1-n2, 2)
def multiplication(n1, n2):
    return round(n1*n2, 2)
def division(n1, n2):
    return round(n1/n2, 2)
def trunacated_division(n1, n2):
    return round(n1//n2, 2)
def modulus(n1, n2):
    return round(n1%n2, 2)
def exponentiation(n1, n2):
    return round(n1**n2, 2)
result=addition(56, 23)
print(result)
result=subtraction(13, 12)
print(result)
result=multiplication(22, 21)
print(result)
result=division(55, 5)
print(result)
result=trunacated_division(124, 2)
print(result)
result=modulus(15,3)
print(result)
result=exponentiation(45.55, 55.25)
print(result)