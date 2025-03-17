num=int(input("enter the number of students : "))
count=1
result=dict()
for count in range(num):
    name=input("enter the name of the student : ")
    percentage=int(input("enter the percentage of the student: "))
    result[name]=percentage
print(result)
find=input("enter the name of the student to be deleted: ")
if find in result:
    del result[find]
    print("new dictionary is :",result)
