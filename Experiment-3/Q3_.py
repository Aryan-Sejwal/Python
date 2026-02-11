term=int(input('enter the number = '))
a,b=0,1
for _ in range (term):
    print(a, end=" ")
    a,b=b,a+b
