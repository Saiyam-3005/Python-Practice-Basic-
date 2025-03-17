#0,1,1,2,3,5.... uinf for and while loop
n=eval(input('no. of terms to be printed :'))
n1=0
n2=1
i=0
print(n1,n2,sep=',',end=',')
for i in range(1,n-1):
    n3=n1+n2
    print(n3,end=',')
    n1,n2=n2,n1
    n2,n3=n3,n2


n=eval(input('no. of terms to be printed :'))
n1=0
n2=1
i=1
print(n1,n2,sep=',',end=',')
while (i<=n-2):
    n3=n1+n2
    print(n3,end=',')
    n1,n2=n2,n1
    n2,n3=n3,n2
    i+=1
input()
    
