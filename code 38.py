n=int(input('number of lines:'))
x=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(x),end=" ")
        x=x+1
    print()
