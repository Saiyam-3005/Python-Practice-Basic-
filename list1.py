n=int(input("enter the number of elements in the list:"))
l=[]
for i in range(0,n):
    x=int(input("enter the number:"))
    l.append(x)
print(l)
def linear():
    n=int(input("enter the number to be searched:"))
    for i in range(len(l)):
        if l[i]==n:
            print("the number is at index value :",i)
print(linear())

 
