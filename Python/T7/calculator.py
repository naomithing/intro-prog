def calculate_sum(x, y):
    """this function takes 2 numbers as inputs and returns their sum"""
    #calculate the sum of the two numbers
    result = x+y
    #return the result
    return result
def calculate_difference(x, y):
    """this function takes 2 numbers as inputs and returns their difference"""
    #calculate the difference of the two numbers
    result = x-y
    return result
def calculate_product(x, y):
    """this function takes 2 numbers as inputs and returns their product"""
    #calculate the product of the two numbers
    result = x*y
    return result
#testign the function with some example of inputs
x = 2
y = 1
sum_result= x+y
difference_result=x-y
product_result=x*y
print(f"the sum of x and y is {sum_result}")
print(f"the difference of x and y is {difference_result}")
print(f"the product of x and y is {product_result}")
