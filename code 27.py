n=eval(input('enter the number to check:'))
for i in range(2,n//2+1):
    if n%i==0:
        print('it is not a prime number')
        break
    else:
        print('it is a prime number')
