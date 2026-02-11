count = 0
for num in range(1, 101):
    if num%5==0 and num%7==0 :
        print(num)
        count += 1

print("Count =", count)
