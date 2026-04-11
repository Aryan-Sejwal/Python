import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
row_sum = np.sum(arr,axis=1)
col_sum = np.sum(arr,axis=0)
flat_arr = arr.flatten()
sorted_arr = np.sort(flat_arr)
second_max = sorted_arr[-2]
print("Sum of rows: ",row_sum)
print("Sum of columns: ",col_sum)
print("Second maximum element is: ",second_max)