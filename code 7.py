'''s1=float(input('marks of english:'))
s2=float(input('marks of maths:'))
s3=float(input('marks of chemistry:'))
s4=float(input('marks of physics:'))
s5=float(input('marks of computer:'))
average=(s1+s2+s3+s4+s5)/5
print('the average marks of the student:',average)
input()'''
import random
sides=["east","west","north","south"]
N=random.randint(1,3)
out=""
for i in range(N,1,-1):
    out=out+sides[i]
print(out)

