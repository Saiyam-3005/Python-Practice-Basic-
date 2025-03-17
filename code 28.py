#371=3**3+7**3+1**3
n=int(input('enter the 3 digit number:'))
a=n//100
b=n//10-(a*10)
c=n-(a*100+b*10)
d=a**3+b**3+c**3
if n==d:
    print('it is a armstong number')
elif n!=d:
    print('it is not a armstrong number')

