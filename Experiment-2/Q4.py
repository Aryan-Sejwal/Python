num_1=int(input('Enter the first number = '))
num_2=int(input('Enter the second number = '))
num_3=int(input('Enter the third number = '))
if num_1>num_2 or num_1>num_3 :
    print(num_1 , 'is greatest among the three numbers')
elif num_2>num_1 or num_2>num_3 :
    print(num_2 , 'is greatest among the three numbers')
else:
    print (num_3 , 'is greatest among the three numbers')