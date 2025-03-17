#plidrome series 15851
o=eval(input('enter a number:')) 
n=o
r=0
while n>0:                        
    d=n%10                    
    r=r*10+d                
    n=int(n/10)             
if o==r:
    print('palidrome')
else:
    print('not a palidrome')

    
