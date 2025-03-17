print('area of circle is =1')
print('area of rectangle is =2')
print('circumfrence of circle is =3')
print('area of square is =4')
w=eval(input('enter your choice:'))
if w==1:
    print('AREA OF CIRCLE')
    r=eval(input('radius of circle:'))
    p=22/7*(r**2)
    print(p)
elif w==2:
     print('AREA OF RECTANGLE')
     i=eval(input('length of rectangle:'))
     q=eval(input('breath of rectangle:'))
     e=i*q
     print(e)
elif w==3:
     print('CIRCUMFRENCE OF CIRCLE')
     u=eval(input('radius of circle:'))
     h=2*(22/7)*u
     print(h)
elif w==4:
     print('AREA OF SQUARE')
     t=eval(input('side of square:'))
     k=(t**2)
     print(k)
else:
    print('invalid choice')
