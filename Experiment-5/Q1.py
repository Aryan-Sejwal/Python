n = int(input("Enter number of values = "))
count_0 = 0
count_1 = 0
count_2 = 0
count_3 = 0
for _ in range(n):
    x= int(input("Enter value (0-3) = "))
    if x == 0:
        count_0 += 1
    elif x == 1:
        count_1 += 1
    elif x == 2:
        count_2 += 1
    elif x == 3:
        count_3 += 1
    else:
        print("Invalid input")

print("0 occurred", count_0, "times")
print("1 occurred", count_1, "times")
print("2 occurred", count_2, "times")
print("3 occurred", count_3, "times")