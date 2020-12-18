a=int(input('Enter Number 1:-'))
b=int(input('Enter Number 2:-'))
c=input('Enter The Operator:-')
if c=='+':
    print('Addition is:-',a+b)
elif c=='-':
    print('Substraction is:-',a-b)
elif c=='*':
    print('Multiplication is:-',a*b)
elif c=='/':
    print('Division is:-',a/b)
else:
    print('Enter Valid Operator')
