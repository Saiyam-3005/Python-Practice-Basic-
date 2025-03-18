def Push(stk,item):
    for i in item:
        stk.append(i)
    
def Pop(stk,item):
    item2=""
    print(item)
    if stk==[]:
        print("Underflow")
        return
    else:
        for j in range(len(stk)-1,-1,-1):
            item2+=stk.pop(j)
        print("Reverse of string is :",item2)
    if item==item2:
        print("it's palindrome")
    else:
        print("it's not palindrome")
    
Stack=[]
item=""
item1=""
print("1:create stack\n2:check palindrome\n3:exit")
while True:
    ch=int(input("ENTER CHOICE:"))
    if ch==1:
        item=(input("enter string:"))
        Push(Stack,item)
    elif ch==2:
        Pop(Stack,item)
    elif ch==3:
        break
    else:
        print("invalid choice")
        
