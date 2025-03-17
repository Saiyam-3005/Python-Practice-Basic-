n=int(input('number of lines:'))
for i in range(1,n+1):
    x=i
    for j in range(1,i+1):
        print(x,end=" ")
        x=x-1
    print()
