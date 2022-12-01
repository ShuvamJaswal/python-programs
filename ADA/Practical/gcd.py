num1,num2=[int(i) for i in input('Enter Two Numbers separated by \',\' : ').split(',')]
for i in range(max(num1,num2),0,-1):
    if num1%i==0 and num2%i==0:
        print(i)
        break