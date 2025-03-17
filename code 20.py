m1=eval(input('marks of english out of 100:'))
m2=eval(input('marks of maths out of 100:'))
m3=eval(input('marks of physics out of 100:'))
m4=eval(input('marks of chemistry out of 100:'))
g=m1+m2+m3+m4
print('total marks is:',g)
p=g/4
if p>33:
    print('you are pass and your percentage is',p)
else:
    print('you are fail and your percentage is ',p)
