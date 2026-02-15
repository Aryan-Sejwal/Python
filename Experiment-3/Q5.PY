num=int(input())
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if num==rev :
  print('The number is paladrome')  
else :  
   print('Number is not paladrome')