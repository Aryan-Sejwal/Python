def soc(n):
    sum=0
    if n>0:
      for i in range(1,n):
         sum+=(i*i*i)
    else:
       print('the input number is not positive')
    return sum
Sum=soc(5) 
print(Sum)       
