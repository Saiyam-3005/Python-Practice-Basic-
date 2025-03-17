num=int(input("enter the number of classes : "))
count=1
school=dict()
for count in range(num):
    name=input("enter the name of the student: ")
    marks=str(input("enter the marks of the student: "))
    school[name]=marks
print(school)
print("\n\nNAME_OF_THE_STUDENT\tMARKS")
for k in school:
    print(k,"\t\t",school[k])
print("\n")
find=input("enter the name of the student to be fined: ")
for i in school:
    if i==find:
        print("name of the student: ",i,"\nmarks of the students: ",school[i])
print("\n")        
y=input("enter the name of the student to be deleted: ")
if find in school:
    del school[y]
    print("new dictionary is :",school)
    print("\n\nNAME_OF_THE_STUDENT\tMARKS")
    for k in school:
        print(k,"\t\t",school[k])


