print('area of \n1.scalence triangle\n2.circle\n3.rectangle\n4.right triangle')
w=int(input('enter the serial number to be printed:'))
if w==1:
    s=eval(input('side 1:'))
    p=eval(input('side 2:'))
    d=eval(input('side 3:'))
    k=s+p+d/2
    print('AREA')
    i=(k*(k-s)*(k-d)*(k-p))**0.5
    print(i)
elif w==2:
    print('AREA OF CIRCLE')
    r=eval(input('radius of circle:'))
    p=22/7*(r**2)
    print(p)
elif w==3:
    print('AREA OF RECTANGLE')
    i=eval(input('length of rectangle:'))
    q=eval(input('breath of rectangle:'))
    e=i*q
    print(e)
elif w==4:
    b=float(input('base of the right triangle:'))
    h=float(input('height of the right angled riangle:'))
    area=(1/2)*b*h
    print('the area of the right angled triangle:',area)
else:
    print('invalid input')
input()
    
