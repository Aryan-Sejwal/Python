n = int(input("Enter a number: "))
original = n
num_digits = 0

temp = n
while temp > 0:
    temp //= 10
    num_digits += 1
total = 0
temp = original

while temp > 0:
    digit = temp % 10
    power = 1
    i = 0
    while i < num_digits:
        power *= digit
        i += 1
    
    total += power
    temp //= 10
if original == total:
    print(original, "is an Armstrong number!")
else:
    print(original,"is not an Armstrong number.")
