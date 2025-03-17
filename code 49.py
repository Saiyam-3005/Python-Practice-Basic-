n=int(input("enter the number of values  : "))
d=dict()
for c in range(0,n):
    v=input("enter the value : ")
    d[c+1]=v
print(d)
u=d.values()
h=sorted(u,reverse = True)
for q in range(0,len(h)):
    print("the highest number is :",h[q])
    if q==1:
        break
    
