d={'a':1,'b':1,'c':1}
unique=lambda d:len(set(d.values()))==1
print(unique(d))