n=int(input('enter the number of terms:'))
list1=[]
for n in range(0,n):
    r=int(input('enter the term:'))
    list1.append(r)
print('your original list is :',list1)
p=list1[len(list1)-1]
count=0
for i in range(len(list1)-1,-1,-1):
            list1[i]=list1[i-1]
            count+=1
list1[0]=p
print(list1)
print("number of count is :",count)
