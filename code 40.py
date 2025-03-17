'''#exponential series 1-x/4!+x^2/6!
n=int(input('number of inputs:'))
x=eval(input('value of x:'))
sum=1
sign=-1
for i in range(2,n+1):
    fact=1
    for j in range(1,2*i+1):
        fact*=j
    sum+=((x**i)/fact)*sign
    sign*=-1
print("The sum of series is",sum)'''

n=int(input('number of inputs:'))
for i in range(n,0):
    for i in range(0,i):
        print("&")
    
