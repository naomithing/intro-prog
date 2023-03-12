def improved_average(a, b, c, d, e):
    """takes five integer parameters."""
    #create a list of the values
    values =[a, b, c, d, e]
    mode = max(set(values), key = values.count)
    median = sorted(values)[2]
    mean = sum (values)/len(values)
    return mode, median, mean
print(improved_average(2, 3, 4, 5, 6))