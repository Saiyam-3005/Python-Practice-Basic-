import math
print("FUNCTIONS\n1.ADD\n2.SUBTRACT\n3.MULTIPLY\n4.DIVISON\n5.LOG\n6.SIN\n7.COS")
k=1
while k==True:
    print("\n")
    n=int(input("enter the number of the function :"))
    if n==1:
        print("ADDITION")
        s=0
        p=int(input("how mny numbers to be added:"))
        for i in range(0,p):
            n1=int(input("enter the number: "))
            s+= n1
        print("your sum is :  ",s)
    if n==2:
        print("SUBTRACTION")
        p=int(input("how mny numbers to be subtracted:"))
        n1=int(input("enter the first number: "))
        d=n1
        for i in range(1,p):
            n1=int(input("enter the number: "))
            d-= n1
        print("your difference is :  ",d)
    if n==3:
        print("MULTIPLICATION")
        s=1
        p=int(input("how mny numbers to be multiplied:"))
        for i in range(0,p):
            n1=int(input("enter the first number: "))
            s*= n1
        print("your product is :  ",s)
    if n==4:
        print("DIVISION")
        n1=int(input("enter the first number: "))
        n2=int(input("enter the second number : "))
        d=n1/n2
        print("your answer is is :  ",d)
    if n==5:
        print("LOG")
        n1=int(input("enter the number: "))
        d=math.log(n1)
        print("your answer is is :  ",d)
    if n==6:
        print("SIN")
        n1=int(input("enter the ange in radians: "))
        d=math.sin(n1)
        print("your answer is is :  ",d)
    if n==7:
        print("COS")
        n1=int(input("enter the first number: "))
        d=math.cos(n1)
        print("your answer is is :  ",d)



 
