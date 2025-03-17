#exponential series 1-x/2!+x^2/3!
n=int(input('number of inputs:'))
p=eval(input('value of x:'))
sum=p
for i in range(1,n):
    fact=1
    for j in range(1,i+1):
        fact*=j
    sum+=((p**((2*i)-1)/fact))
          
print("The sum of series is",sum)
