n=int(input('enter the number of terms:'))
list1=[]
for n in range(0,n):
    r=int(input('enter the term:'))
    list1.append(r)
print('your original list is :',list1)
p=len(list1)
count=0
for i in range(p):
    for j in range(p-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            count+=1
print(list1)
print("number of steps is :",count)
