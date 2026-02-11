num = int(input("Enter a number: "))
shift = int(input("Enter number of shifts: "))

left_shift = num << shift
right_shift = num >> shift

print("Original number:", num)
print("Left shift value:", left_shift)
print("Right shift value:", right_shift)
