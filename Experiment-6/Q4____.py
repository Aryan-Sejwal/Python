def fibo(n,a=0,b=1):
    if n==0:
        return
    print(a)
    fibo(n-1,b,a+b)
n=int(input('enter your number: '))
fibo(n)