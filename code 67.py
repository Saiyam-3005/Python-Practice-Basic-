print("by saiyam jain")
print("MAIN MENU")
print("1.LENGTH OF A STRING\n2.IF PLAIDROME\n3.CHANGE TO UPPERCASE\n4.REVERSE A STRING")
def length(s):
    p=str(s)
    k=len(p)
    return k

def pal(o):
    s=""
    for i in o[::-1]:
        s+=i
    if o==s:
        return("yes")
    else:
        return("no")
def u(l):
    i=l.upper()
    return i
      
def string_reverse(str1):
    rstr1=''
    index=len(str1)
    while index>0:
        rstr1+=str1[index-1]
        index=index-1
    return rstr1
k=1
while k==1:
    h=int(input("ENTER THE SERIAL NUMBER OF THE PROGRAMME:"))
    if h==1:
        s=str(input("enter the string :"))
        print("length of string is :",length(s))
    elif h==2:
         o=str(input("enter the string:"))
         print(pal(o))
    elif h==3:
        l=str(input("enter the string :"))
        print("the string on uppercase is :",u(l))
    elif h==4:
        str1=str(input("enter a string:"))
        print("reverse string is:\n",string_reverse(str1))
    else:
        print("invalid input")

    
    
    








