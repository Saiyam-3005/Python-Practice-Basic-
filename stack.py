s=[]
c="y"
def push():
    a=input("enter element:")
    s.append(a)
def pop():
    if (s==[]):
        print("underflow")
    else:
        print("deleted element is:", s.pop())
def display():
    l=len(s)
    for i in range(l-1,-1,-1):
        print(s[i])
print("1. push")
print("2. pop ")
print("3. display")    
while(c=="y"):
    x=int(input("enter choice:"))
    if x==1:
        push()
    if x==2:
        pop()
    if x == 3:
        display()
    print("*************************")
    print("enter y to continue")
    c=input("enter choice:")
    
    
