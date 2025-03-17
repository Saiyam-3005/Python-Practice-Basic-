'''Write a menu driven program to manipulate the Lists by passing them to user defined function:
(Note: use list functions for list manipulation in UDFs)
1) To append the data to list passed to the function
2) To add multiple elements to list passed to the function
3) To remove the element from the list'''
print("BY SAIYAM JAIN")
print("FIRST CREATE A LIST")
n=int(input("enter the number of elements in the list:"))
list1=[]
for i in range(0,n):
    x=int(input("enter the terms:"))
    list1.append(x)
print (list1)
print("MAIN MENU")
print("1.To append the data to list passed to the function")
print("2.To add multiple elements to list passed to the function")
print("3.To remove the element from the list")
def append():
    i=int(input("enter the number of terms to be added:"))
    for j in range(0,i):
        l=int(input("enter the element:"))
        list1.append(l)
    return list1
def extend():
    l=int(input("enter the number of elements to be added in the list:"))
    list2=[]
    for i in range(0,l):
        k=int(input("enter the terms:"))
        list2.append(k)
    list1.extend(list2)
    return list1
def remove():
    j=int(input("enter the number of element to be removed:"))
    for i in range(0,j):
        g=int(input("enter the number to be removed:"))
        list1.remove(g)
    return list1

k=1
while k==1:
    h=int(input("ENTER THE SERIAL NUMBER OF THE PROGRAMME TO BE RUN:"))
    if h==1:
        print(append())
    elif h==2:
         print(extend())
    elif h==3:
        print(remove())
    else:
        print("invalid input")
      
