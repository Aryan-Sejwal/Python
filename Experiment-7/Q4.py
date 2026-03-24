N = int(input())

for i in range (N):
    try:
        a, b = input().split()
        a = int(a)
        b = int(b)
        
        print(a // b)
    
    except ZeroDivisionError :
        print("Interger division by zero")
    
    except ValueError :
        print("invalid literal for int()")