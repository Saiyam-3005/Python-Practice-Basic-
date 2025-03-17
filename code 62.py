'''Write a menu driven program to do the following tasks with the help of
user-defined functions
1) Find factorial of a number
2) Check if the number is armstrong number or not
3) Fibonacci series upto n terms
4) To calculate & return the sum of the series
    x/1! + x3/3! + x5/5! + x7/7! + …nterms'''
print('MAIN MENU')
print('1.Find Factorial OF A Number')
print("2.Check if the number is armstrong number or not")
print("3.Fibonacci series upto n terms")
print("4.To calculate & return the sum of the series")
print(" x/1! + x3/3! + x5/5! + x7/7! + …nterms")
k=0
while k==0:
    n=int(input("enter the serial number of the progeram to be perfromed:"))
    if n==1:
        p=1
        t=int(input("enter the number for which factorial is reuired:"))
        for i in range(1,t+1,):
            p*=i
        print("factorial is:",p)
    if n==2:
        t=int(input("enter a 3 digit number for which armstrong is to be checked"))
        a=t//100
        b=t//10-(a*10)
        c=t-(a*100+b*10)
        d=a**3+b**3+c**3
        f=a**3+b**3+c**3
        if t==f:
            print("it is armstrong number:")
        else:
            print("it is not armstrong number:")
    if n==3:
        t=int(input("enter the number of terms of the fibonnaci series:"))
        n1=0
        n2=1
        print(n1,n2,sep=",",end=",")
        for i in range(1,t-1,1):
            n3=n1+n2
            n1,n2=n2,n3
            print(n3,end=",")
        print()
    if n==4:
        t=int(input("enter the number of terms of series:"))
        x=float(input("enter the value of x in the series:"))
        s=0
        for i in range(1,2*t,2):
            p=1
            for j in range(1,i+1):
                p*=j
            s+=(x**i/p)
        print("the sum of series is:",s)
        
            
            
            
            
    
            
        
        
            
