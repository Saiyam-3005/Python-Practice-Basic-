top=None
def Push(stk,item):
    global top
    stk.append(item)
    top=len(stk)-1
def Pop(stk):
    global top
    if stk==[]:
        print("Underflow")
    else:
        print("deleted item is :",stk.pop())
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
def Peek(stk):
    if stk==[]:
        print("undeflow stack is empty")
    else:
        print("top most item is :",stk[top])
def Display(stk):
    global top
    if stk==[]:
        print("empty")
    else:
        print(stk[top],"<-top")
        for a in range(top-1,-1,-1):
            print(stk[a])
Stack=[]
print("1:PUSH\n2:POP\n3:PEEK\n4:DISPLAY\n5:EXIT:")
while True:
    ch=int(input("enter choice:"))
    if ch==1:
        item=int(input("enter item:"))
        Push(Stack,item)
        print(top)
    elif ch==2:
        Pop(Stack)
        print(top)
    elif ch==3:
        Peek(Stack)
    elif ch==4:
        Display(Stack)
    elif ch==5:
        break
    else:
        print("invalid choice")
        
