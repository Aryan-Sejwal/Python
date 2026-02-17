#s = input("Enter the string: ")
#s = s.upper()
#count_dict = {}
#for ch in s:
#    if ch.isalpha():  
#        if ch in count_dict:
#            count_dict[ch] += 1
#        else:
#            count_dict[ch] = 1
#for key in sorted(count_dict):
#    print(count_dict[key], key, sep="")
s=input('enter the string :')
count={}
for i in s:
    if i.isalpha():
        cap=i.upper()
        count[cap]=count.get(cap,0)+1
for key in count.keys():
    print(f"{count[key]} {key}", sep="")        