a=float(input('first side of a triangle:'))
b=float(input('second side of a triangle:'))
c=float(input('third side of a triangle:'))
s=a+b+c/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('area of the triangle:',area)
input()
