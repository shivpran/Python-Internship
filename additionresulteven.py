a=int(input('Enter 1st Number:-'))
b=int(input('Enter 2nd Number:-'))
c=input('Enter Operator:-')
if c=='+':
    x=a+b
    if x%2==0:
        print(x,'is Even Number')
    else:
        print(x,'is Odd Number')
elif c=='-':
    y=a-b
    if y%2==0:
       print(y,'is Even Number')
    else:
        print(y,'is Odd Number')
elif c=='*':
    z=a*b
    if z%2==0:
       print(z,'is Even Number')
    else:
        print(z,'is Odd Number')
elif c=='/':
    d=a-b
    if d%2==0:
       print(d,'is Even Number')
    else:
        print(d,'is Odd Number') 
else:
    print('Invalid Operator!')
