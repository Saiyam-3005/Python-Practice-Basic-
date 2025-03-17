num=int(input("enter the number of classes : "))
count=1
school=dict()
for count in range(num):
    clas=input("enter the class: ")
    teacher=str(input("enter the name of the teacher: "))
    school[clas]=teacher
print(school)
print("\n\nCLASS\tTEACHER_NAME")
for k in school:
    print(k,"\t\t",school[k])
find=input("enter the class to be fined: ")
for i in school:
    if i==find:
        print("name of the student: ",i,"\nmarks of the students: ",school[i])
