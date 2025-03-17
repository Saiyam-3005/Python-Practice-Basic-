n=eval(input('enter the number till which you want sum of even numbers:'))
s=0
for i in range(0,n+1,2):
    s+=i
print('the sum of even numbers is :',s)
