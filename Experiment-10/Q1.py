import numpy as np
n = int(input("Enter number of elements: "))
arr = np.array(list(map(int, input("Enter elements: ").split())))
print("Array:", arr)
print("Sum:", np.sum(arr))