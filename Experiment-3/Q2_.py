num=int(input('enter your number = '))
power=len(str(num))
total=0
temp=num
while temp > 0 :
    r=temp%10
    total=total + r**power
    temp=temp//10
if total==num :
    print('the number is amstrong number')
else:
    print('the number is not amstrong number')