n = int(input("Enter number of elements = "))
nums = []
for i in range(n):
    value = int(input("Enter number = "))
    nums.append(value)
t = tuple(nums)
avg = sum(t) / n

print("Tuple =", t)
print("Average =", avg)