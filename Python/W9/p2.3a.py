dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
num = dict(list(dict1.items())+list(dict2.items())+list(dict3.items()))
num.update({7: 70}) #adding the key and dictionary
del num[3]
print(num)
max_value = max(num.values())
min_value = min(num.values())
print("the maximum value is: ", max_value)
print("the minimum value is: ", min_value)

