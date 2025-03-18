Tuple=(1,2,3,4,5,6,7)
n=int(input("enter the elements to be searched:"))
flag=False
for i in range(len(Tuple)):
    if Tuple[i]==n:
        print("element found at index",i)
        flag=True	
if flag==True:
    print("successful search")
else:
    print("not found")
