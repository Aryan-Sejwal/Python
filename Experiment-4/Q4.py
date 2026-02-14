n=input('enter the string: ')
m=input('enter the sub-string: ')
count=0
start=0
while True:
    pos=n.find(m,start)
    if pos ==-1 :
        break
    count+=1
    start=pos+1
print(count)    