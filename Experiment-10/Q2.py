import numpy as np
arr = np.array([[10,20,30],
[40,50,60],
[70,80,90]])
print("Array:\n", arr)
print("Row-wise sum:", arr.sum(axis=1))
print("Column-wise sum:", arr.sum(axis=0))
print("Second maximum:", np.sort(arr.flatten())[-2])