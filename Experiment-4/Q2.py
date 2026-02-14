n=input('Enter your string : ')
count=0
for i in n:
    if i in "aeiou" or i in "AEIOU":
     count+=1
print(count)    