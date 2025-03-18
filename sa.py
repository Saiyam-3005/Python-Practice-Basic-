'''#fibonacci series 0,1,1,2,3,5,8,13...n
x=int(input("enter the number of terms of the series:"))
n1=0
n2=1
print(n1,n2,end=',')
for i in range(1,x-1):
    n3=n1+n2
    n1,n2=n2,n3
    print(n3,end=',')'''




#various function in list to be performed
n=int(input("enter the number of terms in the list :"))
l=[]
for i in range(0,n):
    x=int(input("enter the number :"))
    l.append(x)
print(l)
print("1.append element in the list\n2.add multiple element to list\n3.remove element to the list\n")
r=int(input("enter the serial number of the task to be performed:"))
if r==1:
      g=int(input("enter the number :"))
      l.append(g)
      print(l)
if r==2:
      g=int(input("enter the number of term to be added :"))
      k=[]
      for i in range(0,g):
            x=int(input("enter the number :"))
            k.append(x)
      l.extend(k)
      print(l)
if r==3:
      g=int(input("enter the element from the list to be removed: "))
      l.remove(g)
      print(l)
