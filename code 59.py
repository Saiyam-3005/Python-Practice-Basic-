n=int(input('enter the number of terms:'))
list1=[]
for n in range(0,n):
    r=int(input('enter the term:'))
    list1.append(r)
print('your original list is :',list1)
for i in range(len(list1)):
    if i%2==0:
        list1[i]*=2
    else:
        list1[i]/=2
print(list1)
