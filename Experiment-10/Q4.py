import pandas as pd
a = pd.Series([1,2,3,4])
b = pd.Series([2,2,2,2])
result = a ** b
print("Array1:\n",a)
print("Array2:\n",b)
print("Power:\n",result)