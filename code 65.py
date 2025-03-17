print("MAIN MENU")
print("1.FACTORIAL OF A NUMBER\n2.IF ARMSTRONG OR NOT\n3.FIBONNACI SERIES\n4,SUM OF SERIES")
def fact(num):
    r=1
    for i in range(1,num+1):
       r*=i
    return r

def arm(n):
    a=n//100
    b=n//10-(a*10)
    c=n-(a*100+b*10)
    d=a**3+b**3+c**3
    if n==d:
        f='it is a armstong number'
    elif n!=d:
        f='it is not a armstrong number'
    return f

def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
      
def exp_series(n,x):
    s=0
    for i in range(1,2*n,2):
        p=1
        for j in range(1,i+1):
             p*=j
        s+=(x**i/p)
    return s
k=1
while k==1:
    h=int(input("ENTER THE SERIAL NUMBER OF THE PROGRAMME TO BE RUN:"))
    if h==1:
        num=int(input("enter the number :"))
        print("factorial of number is :",fact(num))
    if h==2:
         n=int(input("enter the number:"))
         print(arm(n))
    if h==3:
        n=int(input("enter the nunber of term :"))
        print("the series is :")
        for i in range(n):
            print(fib(i),sep=',',end=',')
        print("\n")
    if h==4:
        n=int(input('number of inputs:'))  
        x=float(input('value of x:'))
        print("the sum of series is :",exp_series(n,x))

    
    
    




























