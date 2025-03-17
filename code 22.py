a=eval(input('enter the first number'))
b=eval(input('enter the second number'))
o=input('enter the operater symbol ')
if o=='+':
    print('sum is:',a+b)
elif o=='*':
    print('product is:',a*b)
elif o=='-':
    print('difference is:',a-b)
elif o=='/':
    print('divison is:',a/b)
elif o=='//':
    print('float division is:',a//b)
elif o=='**0.5':
    print('square root is:',a**0.5,'\t',b**0.5)
elif o=='%':
    print('remainder is:',a%b)
else:
    print('invalid operater')
