n=int(input('Enter The Number : '))
f=n
s=0
while(f>0):
    a=f%10
    f=f//10
    s=s+(a**3)
if (s==n):
    print('great')
o=n
r=0
while (o>0):                        
    d=o%10                    
    r=r*10+d                
    o=o//10
if n==r:
    print('perfect')
         
