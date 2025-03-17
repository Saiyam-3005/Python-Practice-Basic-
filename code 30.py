'''n=int(input('number of lines:'))
for i in range(1,n+1):
    x=65
    for j in range(1,i+1):
        print(chr(x),end=" ")
        x=x+1
    print()'''
n=int(input('number of lines:'))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("%",end=" ")
    print()

    

