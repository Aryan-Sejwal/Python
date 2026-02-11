n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci series:")
print(a, end=" ")
if n > 1:
    print(b, end=" ")

i = 3  
while i <= n:
    next_term = a + b
    print(next_term, end=" ")
    a = b
    b = next_term
    i += 1

print()  