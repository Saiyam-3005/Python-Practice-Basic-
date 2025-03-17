print("MAIN MENU")
print("1.SIMPLE INTEREST\n2.EXPONENTIAL VALUE\n3.BINARY NUMBER TO DECIMAL\n4.PRIME NUMBERS")
def simple_interest(p,r,t):
    si=p*r*t/100.00
    return si
def exp(x,n):
    e=x**n
    return e
def binaryToDecimal(binary):
      
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal
def prime(v):
    for n in range(1,v):
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    break
            else:
                print(n)
    return n
k=1
while k==1:
    h=int(input("ENTER THE SERIAL NUMBER OF THE PROGRAMME TO BE RUN:"))
    if h==1:
        p=int(input("enter the principal :"))
        print(" simple ineterest of number is :",simple_interest(p,r=10,t=2))
    elif h==2:
         x=int(input("enter the number :"))
         print(exp(x,n=2))
    elif h==3:
        binary=int(input("enter the binary number :"))
        print("the decimal number is :",binaryToDecimal(binary))
    elif h==4:
        print(prime(v=10))
    else:
        print("invalid input")
    
