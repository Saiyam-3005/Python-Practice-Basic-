r=float(input('radius of the circle:'))
a=2*(22/7)*(r**2)
c=2*(22/7)*r
print('the area and circumfrence of the circle are:\n area is:',a,'\n circumfrence is:',c)
input()






















l=[1,2,3,4,5,6,7,8,9,10,-1,-2,-3]
for i in (l):
    if i>=0:
        if i%2==0:
            p=[]
            p.append(i)
        else:
            q=[]
            q.append(i)
    else:
        r=[]
        r.append(i)
print(l)
print(p)
print(q)
print(r)
