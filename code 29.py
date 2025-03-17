n=int(input('Enter Number Of Lines :'))
for i in range(0,n):
    x=1
    for j in range(0,i+1):
        print(x,end=" ")
        x=x+2
    print()
