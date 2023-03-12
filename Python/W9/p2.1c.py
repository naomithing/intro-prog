sum = 0
while True:
    num = int(input("enter number to sum(a neg num to terminate the loop: "))
    if num < 0:
        break
    if num > 100:
        continue
    sum += num
print(sum)
