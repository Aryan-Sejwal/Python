def fibo(term):
    if term==0:
       return
    a,b=0,1
    for _ in range (term):
     print(a, end=" ")
     a,b=b,a+b
n=int(input('enter the number = '))
series=fibo(n)
print(series)

